Add-Type -AssemblyName PresentationFramework
Add-Type -AssemblyName System.Windows.Forms
Add-Type -Name Window -Namespace Win32 -MemberDefinition @"
[DllImport("user32.dll")]
public static extern IntPtr GetWindowDC(IntPtr hWnd);
[DllImport("user32.dll")]
public static extern int ReleaseDC(IntPtr hWnd, IntPtr hDC);
[DllImport("gdi32.dll")]
public static extern int BitBlt(IntPtr hDestDC, int x, int y, int nWidth, int nHeight, IntPtr hSrcDC, int xSrc, int ySrc, int dwRop);
[DllImport("user32.dll")]
public static extern bool GetWindowRect(IntPtr hWnd, out RECT lpRect);
public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
"@

#region ================== FUNCTIONS ==================

function Get-InstalledSoftware {
    [CmdletBinding()]
    param(
        [string]$ComputerName = $env:COMPUTERNAME
    )

    # Normalize computer name (trim whitespace, handle IPs/hostnames uniformly)
    $ComputerName = $ComputerName.Trim()
    
    # Skip connection test for local machine
    if ($ComputerName -ne $env:COMPUTERNAME -and $ComputerName -ne 'localhost' -and $ComputerName -ne '127.0.0.1') {
        # Test connectivity using both ping and port test for better reliability with IPs
        $isReachable = $false
        try {
            # First try quick ping test
            $isReachable = Test-Connection -ComputerName $ComputerName -Count 1 -Quiet -ErrorAction Stop
        } catch {
            # Fallback to port test for firewalled systems (PowerShell remoting port)
            try {
                $tcp = New-Object System.Net.Sockets.TcpClient
                $tcp.Connect($ComputerName, 5985)
                $isReachable = $tcp.Connected
                $tcp.Close()
            } catch {
                $isReachable = $false
            }
        }
        
        if (-not $isReachable) {
            return [PSCustomObject]@{
                ComputerName = $ComputerName
                Name = "Connection Failed"
                Version = "N/A"
                Vendor = "N/A"
                InstallDate = "N/A"
                Status = "Error: Host unreachable (check firewall/PowerShell remoting)"
            }
        }
    }

    try {
        # Using registry for faster and more reliable software enumeration
        $registryPaths = @(
            "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*",
            "SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*"
        )
        
        $software = @()
        
        foreach ($path in $registryPaths) {
            if ($ComputerName -eq $env:COMPUTERNAME -or $ComputerName -eq 'localhost' -or $ComputerName -eq '127.0.0.1') {
                $items = Get-ItemProperty "HKLM:\$path" -ErrorAction SilentlyContinue
            } else {
                $items = Invoke-Command -ComputerName $ComputerName -ScriptBlock {
                    Get-ItemProperty "HKLM:\$using:path" -ErrorAction SilentlyContinue
                } -ErrorAction SilentlyContinue
            }
            
            foreach ($item in $items) {
                if ($item.DisplayName -and $item.DisplayName.Trim()) {
                    $installDate = "Unknown"
                    if ($item.InstallDate) {
                        try {
                            if ($item.InstallDate -match '^\d{8}$') {
                                $installDate = [datetime]::ParseExact($item.InstallDate, "yyyyMMdd", $null).ToString("dd.MM.yyyy")
                            } else {
                                $installDate = [datetime]$item.InstallDate | Out-String
                            }
                        } catch {
                            # Keep default "Unknown"
                        }
                    }
                    
                    $software += [PSCustomObject]@{
                        ComputerName = $ComputerName
                        Name = $item.DisplayName
                        Version = $item.DisplayVersion
                        Vendor = $item.Publisher
                        InstallDate = $installDate
                        Status = "OK"
                    }
                }
            }
        }
        
        # Return empty array if no software found (not error)
        if ($software.Count -eq 0) {
            return @([PSCustomObject]@{
                ComputerName = $ComputerName
                Name = "No software found"
                Version = "N/A"
                Vendor = "N/A"
                InstallDate = "N/A"
                Status = "Warning: Registry query succeeded but no entries found"
            })
        }
        
        return $software
    }
    catch {
        return [PSCustomObject]@{
            ComputerName = $ComputerName
            Name = "Enumeration Error"
            Version = "N/A"
            Vendor = "N/A"
            InstallDate = "N/A"
            Status = "Error: $($_.Exception.Message)"
        }
    }
}

function Export-DataToCSV {
    param(
        [array]$Data,
        [string]$FilePath
    )
    
    try {
        $Data | Export-Csv -Path $FilePath -NoTypeInformation -Encoding UTF8 -Force
        return $true
    }
    catch {
        return $false
    }
}

#endregion

#region ================== XAML ==================

[xml]$XAML = @"
<Window xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="ISWInfo"
        Width="1100"
        Height="900"
        MinWidth="900"
        MinHeight="600"
        ResizeMode="CanResizeWithGrip"
        WindowStyle="None"
        AllowsTransparency="True"
        Background="Transparent"
        WindowStartupLocation="CenterScreen"
        FontFamily="Segoe UI Variable"
        TextOptions.TextFormattingMode="Display"
        TextOptions.TextRenderingMode="ClearType"
        UseLayoutRounding="True">

    <Window.Resources>
        <!-- Gradients -->
        <LinearGradientBrush x:Key="MagentaGradient" StartPoint="0,0" EndPoint="1,1">
            <GradientStop Color="#E20074" Offset="0"/>
            <GradientStop Color="#FF0090" Offset="0.5"/>
            <GradientStop Color="#B3005C" Offset="1"/>
        </LinearGradientBrush>
        
        <LinearGradientBrush x:Key="DarkMagentaGradient" StartPoint="0,0" EndPoint="1,1">
            <GradientStop Color="#B3005C" Offset="0"/>
            <GradientStop Color="#E20074" Offset="1"/>
        </LinearGradientBrush>
        
        <!-- Telekom Magenta glow effect -->
        <DropShadowEffect x:Key="MagentaGlow"
                          Color="#E20074"
                          BlurRadius="25"
                          ShadowDepth="0"
                          Opacity="0.85"/>
                          
        <DropShadowEffect x:Key="DarkMagentaGlow"
                          Color="#B3005C"
                          BlurRadius="25"
                          ShadowDepth="0"
                          Opacity="0.85"/>
                          
        <DropShadowEffect x:Key="WhiteGlow"
                          Color="#FFFFFF"
                          BlurRadius="15"
                          ShadowDepth="0"
                          Opacity="0.7"/>

        <!-- Glass Panel with better visibility -->
        <Style x:Key="GlassPanel" TargetType="Border">
            <Setter Property="CornerRadius" Value="18"/>
            <Setter Property="Padding" Value="16"/>
            <Setter Property="Background">
                <Setter.Value>
                    <LinearGradientBrush StartPoint="0,0" EndPoint="1,1">
                        <GradientStop Color="#DD000000" Offset="0"/>
                        <GradientStop Color="#AA000000" Offset="1"/>
                    </LinearGradientBrush>
                </Setter.Value>
            </Setter>
            <Setter Property="BorderBrush" Value="{StaticResource MagentaGradient}"/>
            <Setter Property="BorderThickness" Value="1"/>
            <Setter Property="Effect" Value="{StaticResource MagentaGlow}"/>
        </Style>

        <!-- Header Text -->
        <Style x:Key="TelekomHeader" TargetType="TextBlock">
            <Setter Property="Foreground" Value="#FFFFFF"/>
            <Setter Property="FontSize" Value="28"/>
            <Setter Property="FontWeight" Value="Bold"/>
            <Setter Property="HorizontalAlignment" Value="Center"/>
            <Setter Property="Effect">
                <Setter.Value>
                    <DropShadowEffect Color="#E20074"
                                      BlurRadius="25"
                                      ShadowDepth="0"
                                      Opacity="0.9"/>
                </Setter.Value>
            </Setter>
        </Style>

        <!-- Buttons - Fixed blur issue with better rendering -->
        <Style TargetType="Button">
            <Setter Property="Foreground" Value="#FFFFFF"/>
            <Setter Property="FontWeight" Value="Bold"/>
            <Setter Property="Cursor" Value="Hand"/>
            <Setter Property="FontSize" Value="14"/>
            <Setter Property="Padding" Value="16,8"/>
            <Setter Property="SnapsToDevicePixels" Value="True"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border x:Name="bd"
                                CornerRadius="14"
                                Background="#16000000"
                                BorderBrush="{StaticResource MagentaGradient}"
                                BorderThickness="1.5"
                                SnapsToDevicePixels="True">
                            <ContentPresenter HorizontalAlignment="Center" 
                                              VerticalAlignment="Center"
                                              SnapsToDevicePixels="True"/>
                        </Border>
                        <ControlTemplate.Triggers>
                            <Trigger Property="IsMouseOver" Value="True">
                                <Setter TargetName="bd" Property="Background" Value="#33E20074"/>
                                <Setter TargetName="bd" Property="BorderBrush" Value="#FF0090"/>
                            </Trigger>
                            <Trigger Property="IsPressed" Value="True">
                                <Setter TargetName="bd" Property="Background" Value="#66E20074"/>
                            </Trigger>
                        </ControlTemplate.Triggers>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>

        <!-- TextBox -->
        <Style TargetType="TextBox">
            <Setter Property="Background">
                <Setter.Value>
                    <LinearGradientBrush StartPoint="0,0" EndPoint="1,1">
                        <GradientStop Color="#33000000" Offset="0"/>
                        <GradientStop Color="#22000000" Offset="1"/>
                    </LinearGradientBrush>
                </Setter.Value>
            </Setter>
            <Setter Property="Foreground" Value="#FFFFFF"/>
            <Setter Property="BorderBrush" Value="{StaticResource MagentaGradient}"/>
            <Setter Property="BorderThickness" Value="1.5"/>
            <Setter Property="Padding" Value="10"/>
            <Setter Property="FontSize" Value="14"/>
            <Setter Property="HorizontalAlignment" Value="Stretch"/>
        </Style>

        <!-- DataGrid with better visibility -->
        <Style TargetType="DataGrid">
            <Setter Property="Background">
                <Setter.Value>
                    <LinearGradientBrush StartPoint="0,0" EndPoint="1,1">
                        <GradientStop Color="#EE000000" Offset="0"/>
                        <GradientStop Color="#AA000000" Offset="1"/>
                    </LinearGradientBrush>
                </Setter.Value>
            </Setter>
            <Setter Property="Foreground" Value="#FFFFFF"/>
            <Setter Property="BorderBrush" Value="{StaticResource MagentaGradient}"/>
            <Setter Property="BorderThickness" Value="1"/>
            <Setter Property="GridLinesVisibility" Value="Horizontal"/>
            <Setter Property="HorizontalGridLinesBrush" Value="#44FFFFFF"/>
            <Setter Property="RowBackground" Value="#33000000"/>
            <Setter Property="AlternatingRowBackground" Value="#44000000"/>
            <Setter Property="HorizontalAlignment" Value="Stretch"/>
            <Setter Property="VerticalAlignment" Value="Stretch"/>
            <Setter Property="AutoGenerateColumns" Value="False"/>
            <Setter Property="CanUserResizeColumns" Value="True"/>
            <Setter Property="CanUserSortColumns" Value="True"/>
            <Setter Property="SelectionMode" Value="Single"/>
            <Setter Property="SelectionUnit" Value="FullRow"/>
            <Setter Property="HeadersVisibility" Value="Column"/>
        </Style>
        
        <!-- DataGrid Header with better visibility -->
        <Style TargetType="DataGridColumnHeader">
            <Setter Property="Background" Value="{StaticResource DarkMagentaGradient}"/>
            <Setter Property="Foreground" Value="#FFFFFF"/>
            <Setter Property="FontWeight" Value="Bold"/>
            <Setter Property="BorderBrush" Value="#E20074"/>
            <Setter Property="BorderThickness" Value="0,0,0,1"/>
            <Setter Property="Padding" Value="10,6"/>
            <Setter Property="FontSize" Value="14"/>
        </Style>
        
        <!-- DataGrid Row with better visibility -->
        <Style TargetType="DataGridRow">
            <Setter Property="Background" Value="#33000000"/>
            <Setter Property="Foreground" Value="#FFFFFF"/>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#33E20074"/>
                </Trigger>
                <Trigger Property="IsSelected" Value="True">
                    <Setter Property="Background" Value="#66E20074"/>
                </Trigger>
            </Style.Triggers>
        </Style>
        
        <!-- DataGrid Cell with better visibility -->
        <Style TargetType="DataGridCell">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="BorderBrush" Value="Transparent"/>
            <Setter Property="BorderThickness" Value="0"/>
            <Setter Property="Padding" Value="8,4"/>
            <Setter Property="Foreground" Value="#FFFFFF"/>
            <Style.Triggers>
                <Trigger Property="IsSelected" Value="True">
                    <Setter Property="Background" Value="Transparent"/>
                    <Setter Property="Foreground" Value="#FFFFFF"/>
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- ProgressBar -->
        <Style x:Key="MagentaProgressBar" TargetType="ProgressBar">
            <Setter Property="Foreground" Value="{StaticResource MagentaGradient}"/>
            <Setter Property="Background" Value="#33000000"/>
            <Setter Property="Height" Value="12"/>
            <Setter Property="BorderThickness" Value="1"/>
            <Setter Property="BorderBrush" Value="{StaticResource MagentaGradient}"/>
        </Style>
        
        <!-- TabControl -->
        <Style TargetType="TabControl">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="BorderThickness" Value="0"/>
        </Style>
        
        <!-- TabItem - White as requested -->
        <Style TargetType="TabItem">
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="TabItem">
                        <Border Name="Border" Background="#33000000" BorderBrush="#FFFFFF" BorderThickness="1,1,1,0" CornerRadius="8,8,0,0">
                            <ContentPresenter x:Name="ContentSite" VerticalAlignment="Center" HorizontalAlignment="Center" ContentSource="Header" Margin="16,6,16,6">
                                <ContentPresenter.ContentTemplate>
                                    <DataTemplate>
                                        <TextBlock Text="{Binding}" Foreground="#FFFFFF" FontWeight="Bold" />
                                    </DataTemplate>
                                </ContentPresenter.ContentTemplate>
                            </ContentPresenter>
                        </Border>
                        <ControlTemplate.Triggers>
                            <Trigger Property="IsSelected" Value="True">
                                <Setter TargetName="Border" Property="Background" Value="#55000000"/>
                                <Setter TargetName="Border" Property="Effect" Value="{StaticResource WhiteGlow}"/>
                            </Trigger>
                            <Trigger Property="IsMouseOver" Value="True" SourceName="Border">
                                <Setter TargetName="Border" Property="Background" Value="#33E20074"/>
                            </Trigger>
                        </ControlTemplate.Triggers>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>
        
        <!-- Close Button -->
        <Style x:Key="CloseButton" TargetType="Button">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="Foreground" Value="#E20074"/>
            <Setter Property="FontWeight" Value="Bold"/>
            <Setter Property="FontFamily" Value="Segoe UI Symbol"/>
            <Setter Property="FontSize" Value="16"/>
            <Setter Property="Width" Value="30"/>
            <Setter Property="Height" Value="30"/>
            <Setter Property="SnapsToDevicePixels" Value="True"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border x:Name="bd" CornerRadius="50" Background="Transparent" SnapsToDevicePixels="True">
                            <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center" SnapsToDevicePixels="True"/>
                        </Border>
                        <ControlTemplate.Triggers>
                            <Trigger Property="IsMouseOver" Value="True">
                                <Setter TargetName="bd" Property="Background" Value="#33E20074"/>
                            </Trigger>
                            <Trigger Property="IsPressed" Value="True">
                                <Setter TargetName="bd" Property="Background" Value="#66E20074"/>
                            </Trigger>
                        </ControlTemplate.Triggers>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>
        
        <!-- Minimize Button -->
        <Style x:Key="MinimizeButton" TargetType="Button">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="Foreground" Value="#E20074"/>
            <Setter Property="FontWeight" Value="Bold"/>
            <Setter Property="FontFamily" Value="Segoe UI Symbol"/>
            <Setter Property="FontSize" Value="16"/>
            <Setter Property="Width" Value="30"/>
            <Setter Property="Height" Value="30"/>
            <Setter Property="SnapsToDevicePixels" Value="True"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border x:Name="bd" CornerRadius="50" Background="Transparent" SnapsToDevicePixels="True">
                            <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center" SnapsToDevicePixels="True"/>
                        </Border>
                        <ControlTemplate.Triggers>
                            <Trigger Property="IsMouseOver" Value="True">
                                <Setter TargetName="bd" Property="Background" Value="#33E20074"/>
                            </Trigger>
                            <Trigger Property="IsPressed" Value="True">
                                <Setter TargetName="bd" Property="Background" Value="#66E20074"/>
                            </Trigger>
                        </ControlTemplate.Triggers>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>

    </Window.Resources>

    <!-- Main Container -->
    <Border CornerRadius="24"
            Background="#000000"
            BorderBrush="{StaticResource MagentaGradient}"
            BorderThickness="1.5"
            Padding="0"
            Effect="{StaticResource MagentaGlow}">
            
        <!-- Window Controls -->
        <DockPanel>
            <StackPanel Orientation="Horizontal" DockPanel.Dock="Top" HorizontalAlignment="Right" Margin="0,8,8,0">
                <Button x:Name="BtnMinimize" Style="{StaticResource MinimizeButton}" Content="&#xE921;" Margin="0,0,5,0"/>
                <Button x:Name="BtnClose" Style="{StaticResource CloseButton}" Content="&#xE8BB;"/>
            </StackPanel>
            
            <Grid Margin="20,10,20,20">
                <Grid.RowDefinitions>
                    <RowDefinition Height="Auto"/> <!-- Header -->
                    <RowDefinition Height="Auto"/> <!-- Input panel -->
                    <RowDefinition Height="*"/>    <!-- Content -->
                    <RowDefinition Height="Auto"/> <!-- Status panel -->
                </Grid.RowDefinitions>

                <!-- HEADER -->
                <StackPanel Grid.Row="0" Margin="0,0,0,20">
                    <TextBlock Text="ISWInfo"
                               Style="{StaticResource TelekomHeader}"
                               FontSize="32"/>
                    <TextBlock Text="SOFTWARE SCANNER"
                               Style="{StaticResource TelekomHeader}"
                               FontSize="24"
                               Margin="0,-10,0,0"/>
                </StackPanel>

                <!-- INPUT PANEL -->
                <Border Grid.Row="1" Style="{StaticResource GlassPanel}" Margin="0,0,0,16">
                    <Grid>
                        <Grid.RowDefinitions>
                            <RowDefinition Height="Auto"/>
                            <RowDefinition Height="Auto"/>
                        </Grid.RowDefinitions>
                        
                        <Grid>
                            <Grid.ColumnDefinitions>
                                <ColumnDefinition Width="Auto"/>
                                <ColumnDefinition Width="*"/>
                                <ColumnDefinition Width="Auto"/>
                            </Grid.ColumnDefinitions>

                            <TextBlock Text="TARGET SYSTEMS"
                                       Foreground="#E20074"
                                       VerticalAlignment="Center"
                                       FontSize="16"
                                       FontWeight="Bold"/>

                            <TextBox x:Name="TxtComputer"
                                     Grid.Column="1"
                                     Margin="16,0"
                                     Height="40"
                                     Text="localhost"
                                     ToolTip="Enter computer names or IP addresses separated by commas (e.g., PC01,192.168.1.10)"/>

                            <Button x:Name="BtnRun"
                                    Grid.Column="2"
                                    Content="INIT SCAN"
                                    Width="140"
                                    Height="40"/>
                        </Grid>
                        
                        <Grid Grid.Row="1" Margin="0,10,0,0">
                            <Grid.ColumnDefinitions>
                                <ColumnDefinition Width="Auto"/>
                                <ColumnDefinition Width="*"/>
                            </Grid.ColumnDefinitions>
                            
                            <TextBlock Text="FILTER"
                                       Foreground="#E20074"
                                       VerticalAlignment="Center"
                                       FontSize="16"
                                       FontWeight="Bold"/>

                            <TextBox x:Name="TxtFilter"
                                     Grid.Column="1"
                                     Margin="16,0"
                                     Height="40"
                                     VerticalContentAlignment="Center"
                                     ToolTip="Filter results by software name or vendor"/>

                        </Grid>
                    </Grid>
                </Border>

                <!-- CONTENT -->
                <TabControl Grid.Row="2" Margin="0,0,0,16">
                    <TabItem Header="RESULTS">
                        <Border Style="{StaticResource GlassPanel}" HorizontalAlignment="Stretch" VerticalAlignment="Stretch">
                            <DataGrid x:Name="GridData"
                                      Margin="5">
                                <DataGrid.Columns>
                                    <DataGridTextColumn Header="Computer" Binding="{Binding ComputerName}" Width="120"/>
                                    <DataGridTextColumn Header="Software Name" Binding="{Binding Name}" Width="300"/>
                                    <DataGridTextColumn Header="Version" Binding="{Binding Version}" Width="120"/>
                                    <DataGridTextColumn Header="Vendor" Binding="{Binding Vendor}" Width="200"/>
                                    <DataGridTextColumn Header="Install Date" Binding="{Binding InstallDate}" Width="120"/>
                                    <DataGridTextColumn Header="Status" Binding="{Binding Status}" Width="*"/>
                                </DataGrid.Columns>
                            </DataGrid>
                        </Border>
                    </TabItem>
                    
                    <TabItem Header="SUMMARY">
                        <Border Style="{StaticResource GlassPanel}" HorizontalAlignment="Stretch" VerticalAlignment="Stretch">
                            <Grid Margin="20">
                                <Grid.RowDefinitions>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="*"/>
                                </Grid.RowDefinitions>
                                
                                <TextBlock x:Name="TxtSummary" Text="No data available yet. Run a scan to see summary."
                                           Foreground="#FFFFFF" FontSize="16" FontWeight="Bold" Margin="0,0,0,20"/>
                                           
                                <TextBlock Grid.Row="1" Text="Top Vendors:" Foreground="#E20074" FontSize="16" FontWeight="Bold" Margin="0,0,0,10"/>
                                <DataGrid x:Name="GridVendors" Grid.Row="2" VerticalAlignment="Stretch" Margin="0,0,0,0"
                                          AutoGenerateColumns="False" CanUserAddRows="False">
                                    <DataGrid.Columns>
                                        <DataGridTextColumn Header="Vendor" Binding="{Binding Name}" Width="*"/>
                                        <DataGridTextColumn Header="Count" Binding="{Binding Count}" Width="100"/>
                                    </DataGrid.Columns>
                                </DataGrid>
                            </Grid>
                        </Border>
                    </TabItem>
                </TabControl>

                <!-- STATUS PANEL -->
                <Border Grid.Row="3" Style="{StaticResource GlassPanel}">
                    <DockPanel>
                        <StackPanel Orientation="Horizontal" DockPanel.Dock="Left">
                            <Button x:Name="BtnExport" Content="EXPORT CSV" Width="140" Height="36" Margin="0,0,12,0"/>
                            <Button x:Name="BtnHelp" Content="HELP" Width="90" Height="36"/>
                        </StackPanel>

                        <StackPanel Orientation="Horizontal" DockPanel.Dock="Right">
                            <TextBlock x:Name="TxtStatus"
                                       Text="READY"
                                       Foreground="#E20074"
                                       VerticalAlignment="Center"
                                       Margin="20,0,12,0"/>
                            <ProgressBar x:Name="ProgressBar"
                                         Style="{StaticResource MagentaProgressBar}"
                                         Width="300"
                                         HorizontalAlignment="Right"/>
                        </StackPanel>
                    </DockPanel>
                </Border>
            </Grid>
        </DockPanel>
    </Border>
</Window>
"@

#endregion

#region ================== GUI LOGIC ==================

# Fixed ScriptBasePath with null check
$ScriptBasePath = if ($PSScriptRoot) { 
    $PSScriptRoot 
} elseif ($MyInvocation.MyCommand.Path) { 
    Split-Path $MyInvocation.MyCommand.Path 
} else { 
    # Fallback to current directory if both are null
    Get-Location 
}

$reader = New-Object System.Xml.XmlNodeReader $XAML
$Window = [Windows.Markup.XamlReader]::Load($reader)

# Window dragging
$Window.Add_MouseLeftButtonDown({ 
    if ($_.Source -eq $Window -or $_.Source.GetType().Name -eq "Border") {
        $Window.DragMove() 
    }
})

# Find controls - REMOVED GridSoftware reference
$TxtComputer = $Window.FindName("TxtComputer")
$TxtFilter = $Window.FindName("TxtFilter")
$BtnRun = $Window.FindName("BtnRun")
$BtnExport = $Window.FindName("BtnExport")
$BtnHelp = $Window.FindName("BtnHelp")
$BtnClose = $Window.FindName("BtnClose")
$BtnMinimize = $Window.FindName("BtnMinimize")
$GridData = $Window.FindName("GridData")
$GridVendors = $Window.FindName("GridVendors")
$TxtStatus = $Window.FindName("TxtStatus")
$TxtSummary = $Window.FindName("TxtSummary")
$ProgressBar = $Window.FindName("ProgressBar")

# Global variables
$Global:LastData = @()
$Global:FilteredData = @()
$Global:CurrentJob = $null
$Global:Timer = $null

# Window control buttons
$BtnClose.Add_Click({ 
    Stop-CurrentJob
    $Window.Close() 
})
$BtnMinimize.Add_Click({ $Window.WindowState = 'Minimized' })

# Window closing event
$Window.Add_Closing({
    Stop-CurrentJob
})

# Function to stop current job and timer
function Stop-CurrentJob {
    if ($Global:Timer) {
        $Global:Timer.Stop()
        $Global:Timer = $null
    }
    
    if ($Global:CurrentJob) {
        Stop-Job $Global:CurrentJob -ErrorAction SilentlyContinue
        Remove-Job $Global:CurrentJob -ErrorAction SilentlyContinue
        $Global:CurrentJob = $null
    }
}

# CRITICAL FIX: UNCONDITIONALLY clear UI on ANY target change
$TxtComputer.Add_TextChanged({
    if (-not $Window.IsLoaded) { return }
    
    $Global:LastData = @()
    $Global:FilteredData = @()
    
    $null = $Window.Dispatcher.Invoke({
        $GridData.ItemsSource = $null
        $GridVendors.ItemsSource = $null
        $TxtFilter.Text = ""
        $TxtSummary.Text = "Enter target and click INIT SCAN"
        $TxtStatus.Text = "READY - TARGET MODIFIED"
        $ProgressBar.IsIndeterminate = $false
        $ProgressBar.Value = 0
    })
})

# Update grid function - FIXED: Handle mixed object types safely
function Update-DataGrid {
    try {
        if ($null -eq $Global:LastData -or $Global:LastData.Count -eq 0) {
            $null = $Window.Dispatcher.Invoke({
                $GridData.ItemsSource = $null
                $TxtStatus.Text = "NO DATA - CLICK INIT SCAN"
                $TxtSummary.Text = "No data available yet. Run a scan to see summary."
                $GridVendors.ItemsSource = $null
            })
            return
        }

        $Global:FilteredData = $Global:LastData

        if ($TxtFilter.Text.Trim()) {
            $filterText = $TxtFilter.Text.ToLower().Trim()
            $Global:FilteredData = $Global:FilteredData | Where-Object { 
                ($_.Name -and $_.Name.ToLower().Contains($filterText)) -or 
                ($_.Vendor -and $_.Vendor.ToLower().Contains($filterText)) -or 
                ($_.ComputerName -and $_.ComputerName.ToLower().Contains($filterText))
            }
        }

        # Update UI
        $null = $Window.Dispatcher.Invoke({
            $GridData.ItemsSource = $Global:FilteredData
            $TxtStatus.Text = "DISPLAYING $($Global:FilteredData.Count) ITEMS"
            Update-Summary
        })
    } catch {
        # Silent error handling
    }
}

# Filter text changed
$TxtFilter.Add_TextChanged({ Update-DataGrid })

# Update summary tab - FIXED: Robust ComputerName extraction
function Update-Summary {
    if ($Global:FilteredData.Count -eq 0) {
        $TxtSummary.Text = "No data available yet. Run a scan to see summary."
        $GridVendors.ItemsSource = $null
        return
    }
    
    # CRITICAL FIX: Handle both PSCustomObject and Hashtable safely
    $computers = @($Global:FilteredData | ForEach-Object { 
        if ($_ -is [System.Management.Automation.PSCustomObject]) {
            $_.ComputerName
        } elseif ($_ -is [System.Collections.Hashtable]) {
            $_['ComputerName']
        } else {
            $_.ComputerName  # Fallback
        }
    } | Where-Object { $_ } | Select-Object -Unique).Count
    
    $software = ($Global:FilteredData | Where-Object { 
        if ($_ -is [System.Management.Automation.PSCustomObject]) { $_.Status -eq "OK" }
        elseif ($_ -is [System.Collections.Hashtable]) { $_['Status'] -eq "OK" }
        else { $_.Status -eq "OK" }
    }).Count
    
    $errors = ($Global:FilteredData | Where-Object { 
        if ($_ -is [System.Management.Automation.PSCustomObject]) { $_.Status -like "Error*" -or $_.Status -like "Warning*" }
        elseif ($_ -is [System.Collections.Hashtable]) { $_['Status'] -like "Error*" -or $_['Status'] -like "Warning*" }
        else { $_.Status -like "Error*" -or $_.Status -like "Warning*" }
    }).Count
    
    $TxtSummary.Text = "Scanned $computers computer(s), found $software software entries, $errors issues."
    
    # Top vendors (only OK status entries with valid vendor names)
    $vendors = $Global:FilteredData | Where-Object { 
        $status = if ($_ -is [System.Management.Automation.PSCustomObject]) { $_.Status } 
                  elseif ($_ -is [System.Collections.Hashtable]) { $_['Status'] } 
                  else { $_.Status }
        
        $vendor = if ($_ -is [System.Management.Automation.PSCustomObject]) { $_.Vendor } 
                  elseif ($_ -is [System.Collections.Hashtable]) { $_['Vendor'] } 
                  else { $_.Vendor }
        
        ($status -eq "OK") -and $vendor -and $vendor.Trim()
    } | Group-Object -Property { 
        if ($_ -is [System.Management.Automation.PSCustomObject]) { $_.Vendor } 
        elseif ($_ -is [System.Collections.Hashtable]) { $_['Vendor'] } 
        else { $_.Vendor }
    } | Sort-Object Count -Descending | Select-Object -First 10 | 
    ForEach-Object { [PSCustomObject]@{ Name = $_.Name; Count = $_.Count } }
    
    $GridVendors.ItemsSource = $vendors
}

# Run scan button
$BtnRun.Add_Click({
    Stop-CurrentJob
    
    # Clear UI before scan
    $null = $Window.Dispatcher.Invoke({
        $GridData.ItemsSource = $null
        $GridVendors.ItemsSource = $null
        $BtnRun.IsEnabled = $false
        $ProgressBar.IsIndeterminate = $true
        $TxtStatus.Text = "SCANNING..."
    })
    
    # Parse targets
    $targets = if ($TxtComputer.Text.Trim()) {
        $TxtComputer.Text.Split(",") | ForEach-Object { $_.Trim() } | Where-Object { $_ }
    } else {
        @("localhost")
    }
    
    try {
        # DIRECT SCAN - no background jobs (simpler, more reliable)
        $allData = @()
        $processed = 0
        
        foreach ($pc in $targets) {
            $null = $Window.Dispatcher.Invoke({
                $TxtStatus.Text = "Scanning $pc ($($processed+1) of $($targets.Count))..."
            })
            
            $result = Get-InstalledSoftware -ComputerName $pc
            $allData += $result
            $processed++
        }
        
        # Convert to consistent PSCustomObjects for UI binding
        $Global:LastData = @()
        foreach ($item in $allData) {
            if ($item -is [System.Collections.Hashtable]) {
                $Global:LastData += [PSCustomObject]@{
                    ComputerName = $item['ComputerName']
                    Name = $item['Name']
                    Version = $item['Version']
                    Vendor = $item['Vendor']
                    InstallDate = $item['InstallDate']
                    Status = $item['Status']
                }
            } else {
                $Global:LastData += $item
            }
        }
        
        # Update UI
        Update-DataGrid
        
        # CRITICAL FIX: Proper error detection (case-insensitive + flexible matching)
        $errorCount = 0
        foreach ($item in $Global:LastData) {
            if ($item.Status -match "(?i)error:|warning:|connection failed") {
                $errorCount++
            }
        }
        
        $null = $Window.Dispatcher.Invoke({
            $ProgressBar.IsIndeterminate = $false
            $ProgressBar.Value = 100
            
            if ($errorCount -gt 0) {
                $TxtStatus.Text = "COMPLETE WITH $errorCount ERROR(S) - $($Global:LastData.Count) TOTAL ITEMS"
            } else {
                $TxtStatus.Text = "COMPLETE - $($Global:LastData.Count) ITEMS FOUND"
            }
            
            $BtnRun.IsEnabled = $true
        })
    }
    catch {
        $null = $Window.Dispatcher.Invoke({
            $TxtStatus.Text = "SCAN ERROR: $($_.Exception.Message)"
            $ProgressBar.IsIndeterminate = $false
            $BtnRun.IsEnabled = $true
        })
    }
})

# Export button
$BtnExport.Add_Click({
    if (-not $Global:FilteredData -or $Global:FilteredData.Count -eq 0) { 
        [System.Windows.MessageBox]::Show("No data to export. Run a scan first.", "Export Error", "OK", "Warning")
        return 
    }
    
    $saveDialog = New-Object System.Windows.Forms.SaveFileDialog
    $saveDialog.Filter = "CSV files (*.csv)|*.csv|All files (*.*)|*.*"
    $saveDialog.Title = "Export Scan Results"
    $saveDialog.FileName = "ISWInfo_Scan_Results_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
    
    if ($saveDialog.ShowDialog() -eq "OK") {
        if (Export-DataToCSV -Data $Global:FilteredData -FilePath $saveDialog.FileName) {
            $TxtStatus.Text = "EXPORTED → $(Split-Path $saveDialog.FileName -Leaf)"
        } else {
            [System.Windows.MessageBox]::Show("Failed to export data. Check permissions.", "Export Error", "OK", "Error")
        }
    }
})

# Help button
$BtnHelp.Add_Click({
    $helpFile = Join-Path $ScriptBasePath "ISWInfoHELP.html"

    if (Test-Path $helpFile) {
        Start-Process $helpFile
    } else {
        [System.Windows.MessageBox]::Show(
            "Help file not found:`n$helpFile`n`nPlace ISWInfoHELP.html in the same folder as this script.",
            "HELP MISSING",
            "OK",
            "Error"
        )
    }
})

# Initialize UI
$null = $Window.Dispatcher.Invoke({
    $TxtStatus.Text = "READY - ENTER TARGET (hostname or IP) AND CLICK INIT SCAN"
    $ProgressBar.IsIndeterminate = $false
    $ProgressBar.Value = 0
    $GridData.ItemsSource = $null
})

#endregion

# Show window
try {
    $null = $Window.ShowDialog()
} finally {
    Stop-CurrentJob
}