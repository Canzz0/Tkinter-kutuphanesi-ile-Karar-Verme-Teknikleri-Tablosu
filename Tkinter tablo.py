import tkinter as tk

root = tk.Tk()
root.title("Karar Verme Teknikleri Dönem Ödevi")

row_label = tk.Label(root, text="alternatif sayısı:")
row_entry = tk.Entry(root)
column_label = tk.Label(root, text="dogal durum sayısı:")
column_entry = tk.Entry(root)
alfa_label = tk.Label(root, text="alfa değeri giriniz(0-1 arası)")
alfa_entry = tk.Entry(root)

table_data=[]

row_label.pack()
row_entry.pack()
column_label.pack()
column_entry.pack()
alfa_label.pack()
alfa_entry.pack()
def create_table():
    num_rows = int(row_entry.get())
    num_columns = int(column_entry.get())
    num_alfa = float(alfa_entry.get())

    # Dinamik olarak bir tablo oluşturun
    table = tk.Frame(root)
    table.pack()
    for  i in range(num_rows):
        for j in range(num_columns):
            # Her hücreye bir Entry widgeti ekleyin
            cell = tk.Entry(table)
            cell.grid(row=i, column=j)
            print(j)
            print(i)
    # Kullanıcının girdiği değerleri satır ve sütunlara yerleştirin
    def analc_table():    
        for i in range(num_rows):
            
            row_data=[]
            for j in range(num_columns):
                cell = table.grid_slaves(int(i),int(j))[0]
                cell.insert(1,"")
                new_data=cell.get()
                row_data.append(new_data)
                cell.delete(0,"end")
            table_data.append(row_data)

        print("EN BÜYÜK DEĞERLER: ")
        maxValues = []
        for i in table_data:
            enBuyukler = [max(i)]
            maxValues.append(enBuyukler)
            print(enBuyukler.__str__())
        print("EN KÜÇÜK DEĞERLER: ")
        minValues = []
        for i in table_data:
            enKucukler = [min(i)]
            minValues.append(enKucukler)
            print(enKucukler.__str__())
        
        print(" ")
    #İYİMSERLİK KAZANÇ
        print("İyimserlik kazanç: " + max(maxValues).__str__())
        iyi_kazanc_label = tk.Label(root, text="İyimserlik kazanç: " + max(maxValues).__str__())
        iyi_kazanc_label.pack()
        print(" ")
    #İYİMSERLİK MALİYET
        print("İyimserlik maliyet: " + min(minValues).__str__())
        iyimal_label = tk.Label(root, text="İyimserlik maliyet: " + min(minValues).__str__())
        iyimal_label.pack()
        print(" ")
    #KÖTÜMSERLİK KAZANÇ
        print("Kötümserlik kazanç: "+max(minValues).__str__())
        kotu_kazanc_label = tk.Label(root, text="Kötümserlik kazanç: "+max(minValues).__str__())
        kotu_kazanc_label.pack()
        print(" ")
    #KÖTÜMSERLİK MALİYET
        print("Kötümserlik maliyet: "+min(maxValues).__str__())
        kotu_mal_label = tk.Label(root, text="Kötümserlik maliyet: "+min(maxValues).__str__())
        kotu_mal_label.pack()
        degerler = []
        #EŞ OLASILIK
        esOla = 1/float(num_columns)
        esOla =float(esOla)
        esOlaDegerleri =[]
        deger = 0
        toplam = 0
        for  degerler in table_data:
            for i in degerler:
                deger = int(float(i) + float(esOla)
                
                toplam += deger
            esOlaDegerleri.append(toplam)
            toplam = 0

        print("Eş olasılık değerleri:" +str(esOlaDegerleri))
        es_deger_label = tk.Label(root, text="Eş olasılık değerleri:" +str(esOlaDegerleri))
        es_deger_label.pack()

        print("Eş olasılık kazanç: "+max(esOlaDegerleri).__str__())
        es_kazanc_label = tk.Label(root, text="Eş olasılık kazanç: "+max(esOlaDegerleri).__str__())
        es_kazanc_label.pack()

        print("Eş olasılık maliyet: "+min(esOlaDegerleri).__str__())
        es_maliyet_label = tk.Label(root, text="Eş olasılık maliyet: "+min(esOlaDegerleri).__str__())
        es_maliyet_label.pack()
        print(" ")


        hurwics =[]
        for degerler in table_data:
            sonuc = float(max(degerler))*float(num_alfa) + float(min(degerler))*(1-float(num_alfa))
            hurwics.append(sonuc)
        #HURWİCS DEĞERLERİ

        print("Hurwics değerleri: "+ hurwics.__str__())
        hurwich_deger_label = tk.Label(root, text="Hurwics değerleri: "+ hurwics.__str__())
        hurwich_deger_label.pack()

        print("Hurwics kazanç: "+max(hurwics).__str__())
        hurwich_kazanc_label = tk.Label(root, text="Hurwics kazanç: "+max(hurwics).__str__())
        hurwich_deger_label.pack()

        print("Hurwics maliyet: "+min(hurwics).__str__())
        hurwich_maliyet_label = tk.Label(root, text="Hurwics maliyet: "+min(hurwics).__str__())
        hurwich_maliyet_label.pack()
        print(table_data)
    button2= tk.Button(root,text="Sonuçlar",fg="white", bg="red", command=analc_table)
    button2.pack()   
button = tk.Button(root, text="Tabloyu Oluştur",fg="white", bg="green", command=create_table)
button.pack()



root.mainloop()
