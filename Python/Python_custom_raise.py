class ISFILE(Exception):
    def __str__(self):
        print("Neden : Girdiğin konum bir klasöre değil de bir dosyaya çıkıyor olmalı .")
        return "THIS IS NOT DIR ."

print("\n\n")
raise ISFILE