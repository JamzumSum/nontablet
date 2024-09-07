import winreg

__all__ = ["set_tablet_mode"]


def set_tablet_mode(*, disable: bool):
    r"""`reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\PriorityControl
    /v ConvertibleSlateMode /d 00000001 /t REG_DWORD /f`"""

    with winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        r"SYSTEM\CurrentControlSet\Control\PriorityControl",
        0,
        winreg.KEY_ALL_ACCESS,
    ) as key:
        winreg.SetValueEx(
            key,
            "ConvertibleSlateMode",
            0,
            winreg.REG_DWORD,
            int(disable),
        )
