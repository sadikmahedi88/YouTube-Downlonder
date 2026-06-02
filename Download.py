import os
import sys
import subprocess

# --- دالة التحميل التلقائي للمكتبات الناقصة ---
def auto_install_dependencies():
    required_libraries = {
        "yt_dlp": "yt-dlp",
        "rich": "rich"
    }
    
    missing_libraries = []
    for module_name, pip_name in required_libraries.items():
        try:
            __import__(module_name)
        except ImportError:
            missing_libraries.append(pip_name)
            
    if missing_libraries:
        print("\n[!] Dynamic environment check: Missing dependencies found.")
        print(f"[!] Automatically installing: {', '.join(missing_libraries)}")
        print("[~] Please wait while we set up the environment...\n")
        
        try:
            # تنفيذ أمر التثبيت بالخلفية بدون إزعاج المستخدم بنصوص كثيرة
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_libraries],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("[+] Environment initialized successfully!\n")
        except Exception:
            # في حال فشل التثبيت الصامت، يتم إظهار الأخطاء للمستخدم لمعرفتها
            print("[X] Automatic installation failed. Trying standard installation...")
            for lib in missing_libraries:
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# تشغيل الفحص والتثبيت التلقائي قبل أي شيء آخر
auto_install_dependencies()

# --- الآن نقوم باستدعاء المكتبات بأمان بعد ضمان وجودها ---
from yt_dlp import YoutubeDL
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

# Initialize Rich Console
console = Console()

def show_logo():
    """Displays a beautiful colored ASCII logo with developer credits"""
    logo_text = """
    ██╗   ██╗████████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      
    ╚██╗ ██╔╝╚══██╔══╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║      
     ╚████╔╝    ██║       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║      
      ╚██╔╝     ██║       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║      
       ██║      ██║       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗ 
       ╚═╝      ╚═╝       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ 
    """
    console.print(Panel(logo_text, title="[bold cyan]YouTube Downloader Pro[/bold cyan]", border_style="bold magenta", expand=False))
    
    # Developer Credits Panel
    credits_text = (
        "[bold white]👨‍💻 Developer :[/bold white] [bold yellow]sadikmahedi88[/bold yellow]\n"
        "[bold white]🌐 GitHub    :[/bold white] [bold green]github.com/sadikmahedi88[/bold green]\n"
        "[bold white]📢 Telegram  :[/bold white] [bold green]t.me/Murphython[/bold green]"
    )
    console.print(Panel(credits_text, title="[bold red]👑 Credits[/bold red]", border_style="bold cyan", expand=False))
    console.print("[bold yellow]⚡ Welcome to the Professional & Smart Downloader Tool! ⚡[/bold yellow]\n")

def get_android_download_path():
    """Determines the download path for Android or falls back to current directory"""
    android_path = '/storage/emulated/0/Download'
    if os.path.exists(android_path):
        return os.path.join(android_path, '%(title)s.%(ext)s')
    return '%(title)s.%(ext)s'

def download_media():
    show_logo()
    
    # Input URL
    url = console.input("[bold green]🔗 Enter YouTube Video URL: [/bold green]").strip()
    if not url:
        console.print("[bold red]❌ Error: URL cannot be empty![/bold red]")
        return

    # 1. Select Type
    console.print("\n[bold blue]🔽 Select Download Type:[/bold blue]")
    console.print(" [1] 🎥 Video")
    console.print(" [2] 🎵 Audio Only")
    type_choice = console.input("[bold white]Choose an option (1 or 2): [/bold white]").strip()

    ydl_opts = {}
    output_template = get_android_download_path()

    if type_choice == '1':
        # 2. Video Quality Options
        console.print("\n[bold blue]🎬 Select Video Quality:[/bold blue]")
        console.print(" [1] 🔥 Best Available Quality")
        console.print(" [2] 📺 Full HD (1080p)")
        console.print(" [3] ⚡ HD (720p)")
        console.print(" [4] 📱 Eco Quality (480p/360p)")
        quality_choice = console.input("[bold white]Enter quality number: [/bold white]").strip()

        if quality_choice == '2':
            video_format = 'bestvideo[height<=1080]+bestaudio/best'
        elif quality_choice == '3':
            video_format = 'bestvideo[height<=720]+bestaudio/best'
        elif quality_choice == '4':
            video_format = 'bestvideo[height<=480]+bestaudio/best'
        else:
            video_format = 'bestvideo+bestaudio/best'

        # 3. Format Options
        console.print("\n[bold blue]📦 Select Output Format:[/bold blue]")
        console.print(" [1] MP4 (Highly Compatible)")
        console.print(" [2] MKV (Lossless Quality)")
        ext_choice = console.input("[bold white]Enter format number (1 or 2): [/bold white]").strip()
        merge_ext = 'mp4' if ext_choice == '1' else 'mkv'

        ydl_opts = {
            'format': video_format,
            'merge_output_format': merge_ext,
            'outtmpl': output_template,
        }

    elif type_choice == '2':
        # Audio Quality Options
        console.print("\n[bold blue]🎵 Select Audio Quality:[/bold blue]")
        console.print(" [1] 💎 Studio High Quality (320 kbps)")
        console.print(" [2] 📻 Standard Quality (192 kbps)")
        console.print(" [3] 📉 Eco Quality / Small Size (128 kbps)")
        audio_quality_choice = console.input("[bold white]Enter quality number: [/bold white]").strip()

        q_map = {'1': '320', '3': '128'}
        chosen_q = q_map.get(audio_quality_choice, '192')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': chosen_q,
            }],
        }
    else:
        console.print("[bold red]❌ Invalid choice! Process cancelled.[/bold red]")
        return

    console.print("\n[bold yellow]⏳ Fetching video information and starting download...[/bold yellow]\n")
    
    # Advanced Rich Progress Bar
    with Progress(
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(bar_width=30, style="black on blue", complete_style="bold green"),
        "[progress.percentage]{task.percentage:>3.0f}%",
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
    ) as progress:
        
        task_id = progress.add_task("[bold magenta]Downloading...[/bold magenta]", total=100, visible=False)

        def progress_hook(d):
            if d['status'] == 'downloading':
                progress.update(task_id, visible=True)
                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
                downloaded_bytes = d.get('downloaded_bytes', 0)
                
                if total_bytes > 0:
                    percentage = (downloaded_bytes / total_bytes) * 100
                    progress.update(task_id, completed=int(percentage))
            elif d['status'] == 'finished':
                progress.update(task_id, completed=100)

        ydl_opts['progress_hooks'] = [progress_hook]
        ydl_opts['quiet'] = True 

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            console.print("\n[bold green]🎉 Download & Processing Completed Successfully 100%![/bold green]")
            console.print("[bold green]📂 File saved directly to your device's 'Download' folder.[/bold green]\n")
        except Exception as e:
            console.print(f"\n[bold red]❌ An error occurred during download: {e}[/bold red]\n")

if __name__ == "__main__":
    download_media()
