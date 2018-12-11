Simple scripts for analytics of futures data from CHRIS database on Quandl.

Requirements:
------------
1. quandl
2. matplotlib
3. seaborn
4. ipykernel


Step by step config manual using Anaconda3 on Windows10:
-----------------------------------------------------

1. Create virtual environment:

conda create -n quandl

2. Activate virtual environment

conda activate quandl

3. Install dependencies:

conda install <package>

where <package> is every package on requirements list (top of this file)

4. Register virtual env kernel for use in Jupyter notebooks

python -m install --user --name quandl

Jupyter restart typically is required for this to take effect.

5. Clone this repo

git clone https://github.com/t1user/wiki_futures

7. Set QUANDL_API_KEY system environment variable to your api key on Quandl

set QUANDL_API_KEY <key_string>
(to make the change permanent it would could be easier to make the change in Windows settings and reboot)

8. Download data (takes couple of minutes to complete)

cd wiki_futures
python quandl_dowloader.py

9. When using Jupyter notebooks make sure you're using correct kernel (if this manual is followed exactly, it should be named: 'quandl')
