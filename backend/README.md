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

Ben [play.min.io](https://play.min.io/) sitesini kullandım.. kendi `minio` sunucunuz var ise `.env` dosyası içerisinde bilgileri güncelleyebilirsiniz. eğer bu siteyi kullanmak isterseniz. Benim oturum bilgilerimin süresi dolabilir bu yüzden aşağıdaki oturum bilgileri ile kendinize bir bucket ve ilgili key'leri oluşturup o bilgiler ile devam etmelisiniz.

Username: `Q3AM3UQ867SPQQA43P2F`

Password: `zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG`

### Postman ayarları

`Droneqube.postman_collection` ve `Droneqube.postman_environment` dosyalarını postman uygulamasında import ederseniz api metotları gelecektir. Kullanıcı oluşturmak için `Auth/Register` metotunu kullanabilirsiniz. Herhangi bir yetkilendirme koymadım kolayca kullanıcı oluşturabilelim diye. `Auth/Login` metotunun Tests kısmında tüm metotlara `JWT` token ayarlaması için ufak bir kod yazdım.

```js
const response = pm.response.json();
console.log(response);
pm.environment.set("access_token", response.access_token);
```

Postman `environment` ve `collection` doğru şekilde yüklediğiniz taktirde kullanıcı oluşturup login istediği attıktan sonra tüm metotları kullanabiliyor olmanız gerekir. `Postman collection` a ilgili `environment` seçmeyi unutmayın.

### API AYARLARI

Eğer `config.py` dosyasının da `DEBUG=False` yaparsanız tüm hata mesajları belirli bir formatta dönecektir.

```python
if (not app.config["DEBUG"]):
    @app.errorhandler(Exception)
    def unhandled_exception(error):
        return handle_error(error, 500)
```

Kullanıcılarda `yetkilendirme` vardır. Default olarak 2 role tanımlanacak. `Admin` ve `User`. Admin kullanıcı tüm metotlara erişebilir. `User` kullanıcı için herhangi bir kısıt koymadım. Ama siz isterseniz ilgili `route` üzerine `@role_required(Roles.Admin)` şeklinde koyarsanız eklenecektir.

```python
@drones_bp.route("/", methods=["GET"])
#jwt gerekli
@jwt_required()
# sadece admin kullanıcı erişebilir. User kullanıcı erişemez
@role_required(Roles.Admin)
def list_drones():
    return DroneController.paginate()
```

### CORS AYARLARI

Frontend uygulamasının doğru çalışabilmesi için frontend adresinizden gelen isteklere izin vermelisiniz.

`.env` dosyası içerisinde `ALLOWED_ORIGINS` değişkenini kendi frontend uygulamanız adresi ile güncelleyiniz.