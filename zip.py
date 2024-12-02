import os
import zipfile 
import pathlib

thisdir = pathlib.Path(__file__).resolve().parent

def main():
    path = thisdir.joinpath("main.zip")
    if path.exists():
        os.remove(path)


    with zipfile.ZipFile(path, "w") as zf:
        zf.write(thisdir.joinpath("content.tex"), "content.tex")
        zf.write(thisdir.joinpath("main.tex"), "main.tex")
        zf.write(thisdir.joinpath("main.bib"), "main.bib")
        zf.write(thisdir.joinpath("main.bbl"), "main.bbl")
        zf.write(thisdir.joinpath("lipics-logo-bw.pdf"), "lipics-logo-bw.pdf")
        zf.write(thisdir.joinpath("cc-by.pdf"), "cc-by.pdf")
        zf.write(thisdir.joinpath("lipics-v2021.cls"), "lipics-v2021.cls")

        figdir = thisdir.joinpath("figures")
        for figpath in figdir.glob("**/*.pdf"):
            zf.write(figpath, f"{figdir.name}/{figpath.relative_to(figdir)}")
        for figpath in figdir.glob("**/*.png"):
            zf.write(figpath, f"{figdir.name}/{figpath.relative_to(figdir)}")



if __name__ == "__main__":
    main()