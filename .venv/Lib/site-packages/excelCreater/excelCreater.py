
from openpyxl import load_workbook
class ExcelTableCreator:
    def __init__(self, filename, data=None, image=None):
        """
        Excel dosyası oluşturur ve başlık, veri, görsel ekler.
        
        :param filename: Çıktı dosyasının adı
        :param header: Başlıklar listesi
        :param data: Veri listesi
        :param image: Eklenecek görsel dosyası (isteğe bağlı)
        """
        

        # Load the existing workbook
        self.workbook = load_workbook(filename)

        # Select the worksheet you want to update
        self.worksheet = self.workbook['Data']

        # Modify the worksheet (e.g., write some data)


        

        columns_width = [20, 80, 100, 40, 40, 50, 50, 30, 90, 100, 80, 80, 80]
        ascii_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in range(len(data)):
            for j in range(len(data[0])):
                print(f"{ascii_uppercase[j]}{i+1},{data[i][j]}")
                self.worksheet[f"{ascii_uppercase[j]}{i+1}"]=str(data[i][j])

        self.workbook.save(filename)
if __name__=="__main__":
    ExcelTableCreator(
        filename="table.xlsx",
        data=[ (1, 'biskrem', '902306304234', 12.0, 14.0, 50000, 'adet', '02:53', '18/07/2024', 'mehmet', 'ürün_alımı', 'selim', 'yarısı nakit'), (2, 'coca cola', '8690645010212', 3.0, 5.0, 10000, 'şişe', '02:53', '18/07/2024', 'ayşe', 'ürün_satışı', 'ahmet', 'kredi kartı'), (3, 'pepsi', '8714789650123', 2.5, 4.5, 15000, 'şişe', '02:53', '18/07/2024', 'ali', 'ürün_satışı', 'veli', 'nakit'), (4, 'fanta', '8690645010223', 3.0, 5.0, 12000, 'şişe', '02:53', '18/07/2024', 'cem', 'ürün_alımı', 'kemal', 'nakit'), (5, 'ulker cikolata', '8690343034321', 5.0, 8.0, 8000, 'kutu', '02:53', '18/07/2024', 'melis', 'ürün_satışı', 'deniz', 'havale'), (6, 'snickers', '5000159440025', 2.0, 3.5, 6000, 'adet', '02:53', '18/07/2024', 'hakan', 'ürün_alımı', 'elif', 'kredi kartı'), (7, 'nestle', '7613035339635', 4.0, 6.0, 7000, 'adet', '02:53', '18/07/2024', 'levent', 'ürün_satışı', 'hasan', 'nakit'), (8, 'milka', '7622200012366', 4.5, 7.0, 6500, 'kutu', '02:53', '18/07/2024', 'gizem', 'ürün_alımı', 'burak', 'havale'), (9, 'dore', '7622300000012', 3.5, 5.5, 11000, 'adet', '02:53', '18/07/2024', 'taner', 'ürün_satışı', 'mert', 'kredi kartı'), (10, 'torku', '8690123456789', 3.0, 5.0, 9000, 'adet', '02:53', '18/07/2024', 'can', 'ürün_alımı', 'buse', 'nakit'), (11, 'eti', '8690100000001', 4.0, 6.0, 12000, 'kutu', '02:53', '18/07/2024', 'selin', 'ürün_satışı', 'dilara', 'havale'), (12, 'pringles', '5028881039250', 7.0, 10.0, 5000, 'kutu', '02:53', '18/07/2024', 'kadir', 'ürün_alımı', 'kerem', 'kredi kartı'), (13, 'lays', '8719200082842', 5.0, 8.0, 7000, 'kutu', '02:53', '18/07/2024', 'ferhat', 'ürün_satışı', 'ozan', 'nakit'), (14, 'doritos', '8714789642023', 6.0, 9.0, 8000, 'kutu', '02:53', '18/07/2024', 'ozlem', 'ürün_alımı', 'metin', 'havale'), (15, 'ruffles', '8714789624021', 5.0, 8.0, 6000, 'kutu', '02:53', '18/07/2024', 'selim', 'ürün_satışı', 'erol', 'kredi kartı'), (16, 'albeni', '8690343000001', 2.5, 4.0, 10000, 'adet', '02:53', '18/07/2024', 'fatih', 'ürün_alımı', 'ayşe', 'nakit'), (17, 'bebeto', '8690343000012', 3.0, 5.0, 11000, 'adet', '02:53', '18/07/2024', 'serkan', 'ürün_satışı', 'can', 'havale'), (18, 'tadelle', '902349304234', 10.0, 20.0, -1000, 'kutu', '02:53', '18/07/2024', 'yavuzhan', 'ürün_alımı', 'can', 'nakit'), (19, 'biskrem', '902306304234', 12.0, 14.0, 50000, 'adet', '02:53', '18/07/2024', 'mehmet', 'ürün_alımı', 'selim', 'yarısı nakit'), (20, 'coca cola', '8690645010212', 3.0, 5.0, 30000, 'şişe', '02:53', '18/07/2024', 'ayşe', 'ürün_satışı', 'ahmet', 'kredi kartı'), (21, 'pepsi', '8714789650123', 2.5, 4.5, 15000, 'şişe', '02:53', '18/07/2024', 'ali', 'ürün_satışı', 'veli', 'nakit'), (22, 'haribo', '4001686300321', 4.0, 6.0, 9000, 'adet', '02:53', '18/07/2024', 'sinem', 'ürün_alımı', 'mehmet', 'kredi kartı'), (23, 'danone', '7613035339646', 2.0, 3.5, 7000, 'kutu', '02:53', '18/07/2024', 'yigit', 'ürün_satışı', 'sevgi', 'nakit'), (24, 'lindt', '7610400012345', 5.0, 8.0, 6000, 'kutu', '02:53', '18/07/2024', 'dilan', 'ürün_alımı', 'salih', 'havale'), (25, 'godiva', '0312901234567', 10.0, 15.0, 3000, 'kutu', '02:53', '18/07/2024', 'muharrem', 'ürün_satışı', 'emre', 'kredi kartı')],
        #image='image.jpg'
    )
