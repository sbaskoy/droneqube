## DRONEQUBE Project

### Backend çalıştırmak için

```bash
git clone https://github.com/sbaskoy/droneqube.git
```

```bash
cd backend
```

> isterseniz burada sanal python ortamı oluşturabilirsiniz veya paketleri ana python ortamına indirip çalıştırabilirsiniz

eğer `venv` paketiniz yoksa pip ile indirmelisiniz.

```bash
python -m venv .venv
```

sanal ortamı aktifleştirmek için

```bash
.venv\Scripts\activate
```

paketleri yüklemek için

```bash
pip install -r requirements.txt

```

flask uygulamasını çalıştırmak için

```bash
python -m flask --app app run --port 8080 --debug
```

veya

```bash
python run.py
```

### MINIO Ayarları

Ben [play.min.io](https://play.min.io/) sitesini kullandım.. kendi `minio` sunucunuz var ise `.env` dosyası içerisinde bilgileri güncelleyebilirsiniz. eğer bu siteyi kullanmak isterseniz. Beni oturum bilgilerimi kullanabilirsiniz veya aşağıdaki oturum bilgileri ile kendinize bir bucket ve ilgili key'leri oluşturup o bilgiler ile devam edebilirsiniz.

Username: `Q3AM3UQ867SPQQA43P2F`

Password: `zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG`
