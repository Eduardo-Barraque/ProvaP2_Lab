from application.model.entity.item import Item, Images
class Item_DAO:
    def __init__(self):
        produto1_img1 = Images( '1','img/item1_img1.jpg')
        produto1_img2 = Images( '2','img/item1_img2.jpg')
        produto1_img3 = Images( '3','img/item1_img3.jpg')
        produto1_img4 = Images( '4', 'img/item1_img4.jpg')
        produto1 = Item('2321312', 'Smartphone Apple iPhone 7 128GB', 
            [produto1_img1], '10', '389.90', '3509.10' )
        
        produto2_img1 = Images( '1', 'img/item2_img1.jpg')
        produto2_img2 = Images( '2', 'img/item2_img2.jpg')
        produto2_img3 = Images( '3', 'img/item2_img3.jpg')
        produto2_img4 = Images( '4', 'img/item2_img4.jpg')
        produto2 = Item('9971', 'Smart TV Samsung Série 4 UN32J4300AG 32 polegadas LED Plana',
            [produto2_img1], '10', '134.11', '1139.90')
        
        produto3_img1 = Images( '1', 'img/item3_img1.jpg')
        produto3 = Item('6717131', 'Câmera Digital Canon EOS Rebel T5i 18.0 Megapixels', 
            [produto3_img1], '10', '235.20', '1999.20')
        
        produto4_img1 = Images( '1', 'img/item4_img1.jpg')
        produto4 = Item('6717132', 'Lenovo IdeaPad 310 80UH0004BR Intel Core i7-6500U 2.5 GHz 8192 MB 1024 GB',
        [produto4_img1], '10', '259.90', '2599.00')
        
        self.__estoque = [produto1, produto2, produto3, produto4]
        
    def estoqueBuscape(self):
        return self.__estoque
    

        