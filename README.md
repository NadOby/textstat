# textstat


Currently works with RUssian but can be adapted to another languages.

book_make_mm.ipynb - for Going over text and creating probability matrix of pairs of words.
Saved in a local file.

book_use_mm.ipynb - Accepts list of word for use, creates probabily matrix for worda in list based on matrix created in previous step.
Softens the probabilities to make result generation more diverse due to very limited vocabulary in the list.

## dependencies

pip install -r requrements.txt

## Usage

If you want to train please provide texts in a "~/books/" directory as a UTF-8 encoded text files.
Run the training notebook. It is prefferable to overlook every step.
Switch to text generatio notebook, run it.
