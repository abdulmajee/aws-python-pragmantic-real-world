import boto3

client = boto3.client('translate', region_name = "us-east-1")

text = "Marmara Üniversitesi Kütüphaneleri olarak başlattığımız Uzaktan Eğitim / Seminerler Serisi kapsamında 22 Mayıs 2020 Cuma günü saat 13.30’da Springer Nature Yazar Çalıştayı gerçekleştirilecektir."

result = client.translate_text(Text = text, SourceLanguageCode = "auto", TargetLanguageCode = "en")
print(result['TranslatedText'])