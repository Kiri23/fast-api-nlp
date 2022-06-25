import subprocess
print('this work')
# pdfimages -png fargo.pdf img/fargo-images-in-pdf
subprocess.run(["pdfimages", '-png', '../../fargo.pdf', '../../img/automated/imageFargo'])