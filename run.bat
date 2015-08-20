python main.py
pandoc output0.markdown -o page1.pdf -V geometry:margin=1in
pandoc output1.markdown -o page2.pdf -V geometry:margin=1in
pandoc output.markdown -o pages.pdf -V geometry:margin=1in
