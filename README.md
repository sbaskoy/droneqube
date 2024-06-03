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
