import os
import subprocess
import sys
import time
import webbrowser


def ensure_console():
    if os.name != "nt":
        return
    if "--keep-console" in sys.argv:
        return
    python = sys.executable
    script = os.path.abspath(__file__)
    for _ in range(10):
        subprocess.Popen([
            "cmd.exe",
            "/c",
            "start",
            "",
            python,
            script,
            "--keep-console",
        ])
    sys.exit(0)

def open_calculator():
    if os.name == "nt":
        subprocess.Popen(["calc.exe"])
    else:
        raise RuntimeError("Ten skrypt działa tylko na Windows")


def open_windows_message():
    if os.name != "nt":
        return
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "GitHub kvbusdev1 :))))))))))", "GitHub kvbusdev1", 0x40)
    except Exception:
        pass


def display_ascii_art():
    if os.name == "nt":
        os.system("title ASCII Art Display")

    art_lines = [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XX                                                                          XX",
        "XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX",
        "XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX",
        "XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX",
        "XX   MMMMMMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMMXX",
        "XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX",
        "XX   MMMMMy''                                                    ''yMMMMM   XX",
        "XX   MMMy'                                                          'yMMM   XX",
        "XX   Mh'                                                              'hM   XX",
        "XX   -                                                                  -   XX",
        "XX                                                                          XX",
        "XX   ::                                                                ::   XX",
        "XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX",
        "XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX",
        "XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX",
        "XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX",
        "XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX",
        "XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX",
        "XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX",
        "XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX",
        "XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX",
        "XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX",
        "XX              o+++     ++++Mo    M      M    oM++++     +++o              XX",
        "XX                                oo      oo                                XX",
        "XX           oM                 oo          oo                 Mo           XX",
        "XX         oMMo                M              M                oMMo         XX",
        "XX       +MMMM                 s              s                 MMMM+       XX",
        "XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX",
        "XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX",
        "XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX",
        "XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX",
        "XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX",
        "XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX",
        "XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX",
        "XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX",
        "XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX",
        "XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX",
        "XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX",
        "XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX",
        "XX   MMMMMMMM-                                                  -MMMMMMMM   XX",
        "XX   MMMMMMMMM                                                  MMMMMMMMM   XX",
        "XX   MMMMMMMMMy              GitHub kvbusdev1 :)                                  yMMMMMMMMM   XX",
        "XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX",
        "XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX",
        "XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX",
        "XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX",
        "XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX",
        "XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX",
        "XX                                                                          XX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "",
        "    .o88o.                               o8o                .",
        "    888 `\"                               `\"'              .o8",
        "   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo",
        "    888    d88(  \"8 d88' `88b d88' `\"Y8 `888  d88' `88b   888    `88.  .8'",
        "    888    `\"Y88b.  888   888 888        888  888ooo888   888     `88..8'",
        "    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'",
        "   o888o   8\"\"\"888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   \"888\"      d8'",
        "                                                                .o...P'",
        "                                                                `XER0'",
    ]

    for line in art_lines:
        print(line)


def open_browser_with_video(url):
    env = os.environ
    program_files = env.get("PROGRAMFILES", r"C:\Program Files")
    program_files_x86 = env.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)")
    local_appdata = env.get("LOCALAPPDATA", os.path.join(env.get("USERPROFILE", r"C:\Users\%USERNAME%"), "AppData", "Local"))

    raw_paths = [
        # Brave
        r"%PROGRAMFILES%\BraveSoftware\Brave-Browser\Application\brave.exe",
        r"%PROGRAMFILES(X86)%\BraveSoftware\Brave-Browser\Application\brave.exe",
        os.path.join(local_appdata, r"Programs\BraveSoftware\Brave-Browser\Application\brave.exe"),
        os.path.join(local_appdata, r"BraveSoftware\Brave-Browser\Application\brave.exe"),
        # Chrome
        r"%PROGRAMFILES%\Google\Chrome\Application\chrome.exe",
        r"%PROGRAMFILES(X86)%\Google\Chrome\Application\chrome.exe",
        os.path.join(local_appdata, r"Google\Chrome\Application\chrome.exe"),
        os.path.join(local_appdata, r"Programs\Google\Chrome\Application\chrome.exe"),
        # Firefox
        r"%PROGRAMFILES%\Mozilla Firefox\firefox.exe",
        r"%PROGRAMFILES(X86)%\Mozilla Firefox\firefox.exe",
        os.path.join(local_appdata, r"Mozilla Firefox\firefox.exe"),
        # Opera
        r"%PROGRAMFILES%\Opera\launcher.exe",
        r"%PROGRAMFILES(X86)%\Opera\launcher.exe",
        os.path.join(local_appdata, r"Programs\Opera\launcher.exe"),
        os.path.join(local_appdata, r"Opera\launcher.exe"),
        # Edge
        r"%PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe",
        r"%PROGRAMFILES(X86)%\Microsoft\Edge\Application\msedge.exe",
        os.path.join(local_appdata, r"Microsoft\Edge\Application\msedge.exe"),
        os.path.join(local_appdata, r"Programs\Microsoft\Edge\Application\msedge.exe"),
        r"%PROGRAMFILES%\Microsoft\Edge Beta\Application\msedge.exe",
        r"%PROGRAMFILES%\Microsoft\Edge Dev\Application\msedge.exe",
        r"%PROGRAMFILES(X86)%\Microsoft\Edge Beta\Application\msedge.exe",
        r"%PROGRAMFILES(X86)%\Microsoft\Edge Dev\Application\msedge.exe",
    ]

    paths = []
    for path in raw_paths:
        expanded = os.path.expandvars(path)
        expanded = os.path.normpath(expanded)
        if expanded not in paths:
            paths.append(expanded)

    opened = False
    for path in paths:
        if os.path.exists(path):
            args = [path]
            basename = os.path.basename(path).lower()
            if "firefox" in basename:
                args += ["-new-window", url]
            else:
                args += ["--new-window", url]
            subprocess.Popen(args)
            opened = True

    if not opened:
        webbrowser.open(url)

if __name__ == "__main__":
    ensure_console()
    display_ascii_art()
    open_windows_message()
    youtube_url = "https://www.youtube.com/watch?v=L36INNoy_II"
    open_calculator()
    time.sleep(1)
    open_browser_with_video(youtube_url)
    input("\nNaciśnij Enter, aby zakończyć...")