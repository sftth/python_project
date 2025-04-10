# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from naver_stock.services.ht_stock import ht_save_xlsx
from naver_stock.services.nh_stock import nh_save_xlsx
from naver_stock.services.mn_stock import mn_save_xlsx

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("🔄 Starting save xlsx for ht...")
    ht_save_xlsx()
    print("✅ Save xlsx for ht completed.")

    print("🔄 Starting save xlsx for nh...")
    nh_save_xlsx()
    print("✅ Save xlsx for nh completed.")

    print("🔄 Starting save xlsx for mn...")
    mn_save_xlsx()
    print("✅ Save xlsx for mn completed.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
