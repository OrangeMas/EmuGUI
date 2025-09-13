from translations.systemdefaultset import *

def translateMainZH_CN(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "主菜单") # Main
    window.tabWidget.setTabText(1, "设置") # Settings

    # Main tab
    window.pushButton_8.setText("新建虚拟机") # New virtual machine
    window.pushButton_9.setText("启动虚拟机") # Start virtual machine
    window.pushButton_10.setText("编辑选定的虚拟机") # Edit selected virtual machine
    window.pushButton_11.setText("删除选定的虚拟机") # Delete selected virtual machine
    window.pushButton_22.setText("导出选定的虚拟机") # Export selected virtual machine
    window.pushButton_23.setText("导入虚拟机") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "常规") # General
    window.tabWidget_2.setTabText(3, "关于 EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("语言") # Language
    window.pushButton_15.setText("应用") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("System default", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("System default", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("qemu-img 路径") # qemu-img Path
    window.label_2.setText("qemu-system-i386 路径") # qemu-system-i386 Path
    window.label_3.setText("qemu-system-x86_64 路径") # qemu-system-x86_64 Path
    window.label_4.setText("qemu-system-ppc 路径") # qemu-system-ppc Path
    window.label_5.setText("qemu-system-mips64el 路径") # qemu-system-mips64el Path
    window.label_9.setText("qemu-system-aarch64 路径") # qemu-system-aarch64 Path
    window.label_11.setText("qemu-system-arm 路径") # qemu-system-arm Path
    window.label_16.setText("qemu-system-ppc64 路径") # qemu-system-ppc64 Path
    window.label_17.setText("qemu-system-mipsel 路径") # qemu-system-mipsel Path
    window.label_18.setText("qemu-system-mips 路径") # qemu-system-mips Path
    window.label_19.setText("qemu-system-mips64 路径") # qemu-system-mips64 Path
    window.label_12.setText("qemu-system-sparc 路径") # qemu-system-sparc Path
    window.label_13.setText("qemu-system-sparc64 路径") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("qemu-system-alpha 路径") # qemu-system-alpha Path
    window.lbl_riscv32.setText("qemu-system-riscv32 路径") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("qemu-system-riscv64 路径") # qemu-system-riscv64 Path

    window.pushButton.setText("浏览") # Browse
    window.pushButton_2.setText("浏览") # Browse
    window.pushButton_3.setText("浏览") # Browse
    window.pushButton_4.setText("浏览") # Browse
    window.pushButton_5.setText("浏览") # Browse
    window.pushButton_7.setText("浏览") # Browse
    window.pushButton_12.setText("浏览") # Browse
    window.pushButton_16.setText("浏览") # Browse
    window.pushButton_17.setText("浏览") # Browse
    window.pushButton_18.setText("浏览") # Browse
    window.pushButton_19.setText("浏览") # Browse
    window.pushButton_13.setText("浏览") # Browse
    window.pushButton_14.setText("浏览") # Browse
    window.btn_alpha.setText("浏览") # Browse
    window.btn_riscv32.setText("浏览") # Browse
    window.btn_riscv64.setText("浏览") # Browse
    window.pushButton_6.setText("应用") # Apply
    window.btn_apply_qemu2.setText("应用") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("基于 Python 和 PyQt 技术，遵循 GNU 通用公共许可证 3.0")

    window.label_10.setText(
        """
        警告：根据适用法律，本程序不提供任何形式的担保。有关详细信息，请参阅 GNU GPL 许可证。
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("项目由 Tech-FZ. 提供") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI 的媒体平台(英语)") # EmuGUI on social media (in English)

def translateNewVmZH_CN(window):
    window.setWindowTitle("EmuGUI - 创建新的虚拟机") # EmuGUI - Create new VM

    # First page
    window.lbl_vmname.setText("名称") # Name
    window.lbl_arch.setText("架构") # Architecture
    window.cb_arch.setPlaceholderText("请选择架构") # Please choose an architecture

    window.btn_next1.setText("下一步 >") # Next >
    window.btn_cancel1.setText("取消") # Cancel

    # Second page
    window.lbl_machine.setText("机器类型") # Machine
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_ram.setText("内存 (MB)") # RAM in MB

    window.cb_machine.setPlaceholderText("请选择一台虚拟机") # Please select a machine
    window.cb_cpu.setPlaceholderText("请选择一个处理器") # Please select a processor

    window.pb_prev2.setText("< 上一步") # < Previous
    window.pb_next2.setText("下一步 >") # Next >
    window.pb_cancel2.setText("取消") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("VHD 使用情况") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "创建一个新的虚拟硬盘") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "添加一个现有的虚拟硬盘") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "不添加虚拟硬盘") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("VHD 路径") # VHD path
    window.lbl_vhdF.setText("VHD 文件格式") # VHD file format
    window.lbl_maxsize.setText("最大大小") # Maximum size
    window.lbl_hddC.setText("HDD 控制器") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(请选择一个文件格式)") # (Please select a file format)

    window.btn_vhdP.setText("浏览") # Browse
    window.btn_prev3.setText("< 上一步") # < Previous
    window.btn_next3.setText("下一步 >") # Next >
    window.btn_cancel3.setText("取消") # Cancel

    # Fourth page
    window.lbl_vga.setText("图形") # VGA
    window.lbl_net.setText("网络") # Network
    window.lbl_mouse.setText("鼠标") # Mouse
    window.cb_vga.setItemText(0,"由 QEMU 决定") # VGA - Let QEMU decide
    window.label_18.setText("USB 平板设备") # USB Device Tablet
    window.checkBox.setText("启用(已弃用)") # Yes, i want it (depreciated)
    window.cb_mouse.setItemText(0, "PS/2 鼠标")
    window.cb_mouse.setItemText(1, "USB 鼠标")
    window.cb_mouse.setItemText(2, "USB 平板设备")

    window.cb_vga.setPlaceholderText("(请选择图形适配器)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(请选择网络适配器)") # (Please select a network adapter)

    window.btn_prev4.setText("< 上一步") # < Previous
    window.btn_next4.setText("下一步 >") # Next >
    window.btn_cancel4.setText("取消") # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "外部 BIOS 文件位置 \n(留空以使用默认 BIOS)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("外部 BIOS 文件") # External BIOS file

    window.btn_biosF.setText("浏览") # Browse
    window.btn_prev5.setText("< 上一步") # < Previous
    window.btn_next5.setText("下一步 >") # Next >
    window.btn_cancel5.setText("取消") # Cancel

    # Sixth page
    window.lbl_sound.setText("声卡") # Sound card
    window.lbl_cores.setText("CPU 核心数")# CPU cores
    window.lbl_kbd.setText("键盘") # Keyboard
    window.lbl_kbdlayout.setText("键盘布局") # Keyboard layout
    window.cb_kbd.setItemText(0, "PS/2 键盘")
    window.cb_kbd.setItemText(1, "USB  键盘")

    window.btn_prev6.setText("< 上一步") # < Previous
    window.btn_next6.setText("下一步 >") # Next >
    window.btn_cancel6.setText("取消") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Linux 内核") # Linux kernel
    window.lbl_initrd.setText("Linux initrd 镜像") # Linux initrd image
    window.lbl_cmd.setText("Linux 启动参数") # Linux cmd args
    window.lbl_leave.setText("如果不需要请直接单击下一步") # Leave empty if these aren't necessary

    window.btn_kernel.setText("浏览") # Browse
    window.btn_initrd.setText("浏览") # Browse
    window.btn_prev7.setText("< 上一步") # < Previous
    window.btn_next7.setText("下一步 >") # Next >
    window.btn_cancel7.setText("取消") # Cancel

    # Eighth page
    window.lbl_accel.setText("虚拟化加速器") # Acceleration
    window.lbl_cdc1.setText("CD 控制器 1") # CD controller 1
    window.lbl_cdc2.setText("CD 控制器 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< 上一步") # < Previous
    window.btn_next8.setText("下一步 >") # Next >
    window.btn_cancel8.setText("取消") # Cancel

    # Ninth page
    window.lbl_addargs.setText("附加参数（如有需要）") # Additional arguments (if needed)

    window.checkBox_2.setText("我想安装 Windows 2000\n（已弃用）") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("添加 USB 支持") # Add USB support

    window.btn_prev9.setText("< 上一步") # < Previous
    window.btn_finish.setText("完成") # Finish
    window.btn_cancel9.setText("取消") # Cancel

def translateStartVmZH_CN(window, vmname):
    window.setWindowTitle(f"EmuGUI - 启动 {vmname}")
    window.label_4.setText("日期和时间") # Date & Time
    window.label_3.setText("启动方式") # Boot from
    window.label_6.setText("TPM 路径（仅限 Linux）") # TPM path (Linux only)
    window.label_7.setText("请从终端创建 TPM！") # Create the TPM from the terminal!

    window.label_5.setText("""
    注意：如果虚拟机在五分钟内未启动，则应检查虚拟机和 QEMU 设置。
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("浏览") # Browse
    window.pushButton_2.setText("浏览") # Browse
    window.pushButton_6.setText("浏览") # Browse
    window.pushButton_5.setText("设置到系统") # Set to system
    window.pushButton_3.setText("启动虚拟机") # Start VM
    window.pushButton_4.setText("取消") # Cancel
    window.checkBox.setText("使用 RTC 选项") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

def translateVmExistsZH_CN(window):
    window.label.setText(
        "抱歉，具有此名称的虚拟机已存在。"
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "请考虑删除该虚拟机或考虑一个新名称。"
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("好") # OK

def translateVhdExistsZH_CN(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "抱歉，您要创建的磁盘已经存在。"
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("您想保留还是覆盖它？") # Do you want to keep or overwrite it?

    window.pushButton.setText("覆盖") # Overwrite
    window.pushButton_2.setText("保留") # Keep

'''
### No implementation found for this method

def translateSettingsPendingZH_CN(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("没有设置 QEMU 的路径")
    window.label_2.setText("请转到设置以执行此操作，然后再试一次。")

    window.pushButton.setText("OK") # OK
    
'''

def translateVmTooNewZH_CN(window):
    window.label.setText(
        "此虚拟机使用的 EmuGUI 版本过旧。请使用更高版本！"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingZH_CN(window, arch):
    window.label.setText(
        f"抱歉，EmuGUI没有配置使用 \"qemu-system-{arch}\"\n此组件对于启动此虚拟机是必需的。\n请转到设置/QEMU以解决此问题。"
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingZH_CN(window):
    window.label.setText(
        "抱歉，EmuGUI没有配置使用 \"qemu-img\" \n此组件对于创建或编辑虚拟机是必需的。\n请转到设置/QEMU以解决此问题。"
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMZH_CN(window, vmname):
    window.setWindowTitle(f"EmuGUI - 编辑 {vmname}")

    # Buttons on all tabs
    window.btn_cancel.setText("取消") # Cancel
    window.btn_ok.setText("确定") # OK

    # Tab names
    window.tabWidget.setTabText(0, "常规") # General
    window.tabWidget.setTabText(1, "机器") # Machine
    window.tabWidget.setTabText(2, "虚拟硬盘") # Virtual hard disks
    window.tabWidget.setTabText(3, "外设") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "附加组件") # Additional components

    # Translations for General tab
    window.lbl_name.setText("名称") # Name
    window.lbl_arch.setText("架构") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_machine.setText("机器类型") # Machine
    window.lbl_ram.setText("内存大小 (MB)") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("VHD 使用情况") # VHD usage
    window.lbl_vhdp.setText("VHD 路径") # VHD path
    window.lbl_vhdf.setText("VHD 文件格式") # VHD file format
    window.lbl_maxsize.setText("最大大小") # Maximum size
    window.btn_vhdp.setText("浏览") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "创建一个新的虚拟硬盘") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "添加一个现有的虚拟硬盘") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "不添加虚拟硬盘") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("CD 控制器 1") # CD controller 1
    window.lbl_cdc2.setText("CD 控制器 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("HDD 控制器") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "由 QEMU 决定") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("鼠标类型") # Mouse type
    window.lbl_kbdtype.setText("键盘类型") # Keyboard type
    window.lbl_kbdlayout.setText("键盘布局") # Keyboard layout
    window.checkBox_2.setText("USB 平板设备 (已弃用)") # USB Device Tablet
    window.cb_kbdtype.setItemText(0, "PS/2 键盘")
    window.cb_kbdtype.setItemText(1, "USB  键盘")

    window.cb_mouse.setItemText(0, "PS/2 鼠标")
    window.cb_mouse.setItemText(1, "USB 鼠标")
    window.cb_mouse.setItemText(2, "USB 平板设备")

    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("外部 BIOS 文件位置 (留空以使用默认 BIOS)")
    window.lbl_biosf.setText("外部 BIOS 文件") # External BIOS file
    window.btn_biosf.setText("浏览") # Browse

    # Translations for Linux tab
    window.lbl_kernel.setText("Linux 内核") # Linux kernel
    window.lbl_initrd.setText("Linux initrd 镜像") # Linux initrd image
    window.lbl_cmd.setText("Linux 启动参数") # Linux cmd arguments
    window.btn_kernel.setText("浏览") # Browse
    window.btn_initrd.setText("浏览") # Browse

    # Translations for Additional components tab
    window.lbl_vga.setText("图形") # VGA
    window.lbl_net.setText("网络适配器") # Network adapter
    window.lbl_sound.setText("声卡") # Sound card
    window.lbl_addargs.setText("附加参数 (如果需要)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("CPU 核心数") # CPU cores
    window.chb_usb.setText("添加 USB 支持") # Add USB support
    window.lbl_accel.setText("虚拟化加速器") # Acceleration
    window.checkBox_3.setText("我想安装 Windows 2000\n（已弃用）") # I want to install Windows 2000\n(depreciated)



def translateErrDialogZH_CN(window, errcode):
    window.setWindowTitle(f"EmuGUI - 错误")
    
    if errcode.startswith("C"):
        window.label.setText("EmuGUI 遇到严重错误并需要关闭。") # EmuGUI encountered a critical error and needs to be closed.

    elif errcode.startswith("E"):
        window.label.setText("EmuGUI 遇到错误。") # EmuGUI encountered an error.

    elif errcode.startswith("W"):
        window.label.setText("EmuGUI 必须警告您。") # EmuGUI has to warn you.

    else:
        window.label.setText("EmuGUI 有话要说。") # EmuGUI has something to say.

    window.label_2.setText("错误代码: " + errcode) # Error Code:

    window.label_3.setText(
        "如果此错误多次发生，请联系您的管理员或在 EmuGUI Discord 服务器或其 GitHub 存储库上寻求帮助。"
        ) # If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.
    
    window.pushButton.setText("确定") # OK