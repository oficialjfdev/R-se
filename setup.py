import cx_Freeze
executables = [cx_Freeze.Executable("rise.py", icon = "icone.ico")]

cx_Freeze.setup(
    name="RISE", 
    options={"build_exe": {"packages": ["pygame", "moviepy", "sys", "random", "pkg_resources.py2_warn"],
                            "include_files": [("img", "img"),
                            ("audio", "audio"),
                            ("CAPITULO_4_TITULO.mp4",  "CAPITULO_4_TITULO.mp4"),
                            ("CUTSCENE_1.mp4", "CUTSCENE_1.mp4"),
                            ("CUTSCENE_2.mp4", "CUTSCENE_2.mp4"),
                            ("CUTSCENE_3.mp4", "CUTSCENE_3.mp4"),
                            ("CUTSCENE_4.mp4", "CUTSCENE_4.mp4"),
                            ("CUTSCENE_5.mp4", "CUTSCENE_5.mp4"),
                            ("CUTSCENE_6.mp4", "CUTSCENE_6.mp4"),
                            ("CUTSCENE_BONUS.mp4", "CUTSCENE_BONUS.mp4"),
                            ("CUTSCENE_TRAN.mp4", "CUTSCENE_TRAN.mp4")]}},
    executables=executables
)
