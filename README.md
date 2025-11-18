Link ke PWS = https://rehema-zurafa-allfootballstop.pbp.cs.ui.ac.id/
details>
<summary>Tugas 9</summary>
Membuat model Dart untuk interaksi JSON dibandingkan langsung menggunakan Map membuat input lebih aman pertama dengan menggunakan model membuat tipe dari input JSON teratur (Type Safe). Selain itu, adanya model bisa memastikan bahwa input dihandle secara aman dan tidak memiliki point ke null (Null Safety). Penggunaan model juga memudahkan developer dalam mengubah atau memaintain hal-hal yang terkait dengan interaksi JSON.

HTTP berperan sebagai alat komunikasi untuk mengirim dan menerima data dari Internet (alamat server). Sementara CookieRequest diperlukan untuk melakukan session handling (status login).

Alasan CookieRequest harus disimpan diberikan semua komponen di aplikasi Flutter adalah untuk menjaga session yang digunakan oleh semua komponen di flutter sama dan tidak ada yang membuat koneksi baru sendiri.

Agar aplikasi flutter dapat berinteraksi dengan server Django pertama adalah dengan mengonfiguarasikan ALLOWED_HOSTS. Penambahan 10.0.2.2 ke ALLOWED_HOSTS dilakukan sehingga jika ada permintaan dari host 10.0.2.2 (emulator Android Flutter), server Django membolehkan host tersebut untuk melakukan permintaannya. Selanjutnya diperlukan pengonfigurasian CORS.  Tujuannya adalah agar permintaan dari Flutter diberikan oleh server Django. Kemudian diperlukan pengaturan SameSite dan Cookie. Ini diperlukan agar atribut Cookie dan sessionid Django diberikan ke Flutter sehingga hal-hal yang memerlukan Cookie (seperti form) dapat berjalan. Terakhir mengonfigurasi android sehingga memperbolehkan untuk mengakses Internet sehingga aplikasi yang dibuat dapat berinteraksi dengan Internet di Android.

Alur data di flutter:
Pertama, input dari flutter akan diproses oleh widget yang berkaitan. Lalu, Widget akan meminta data JSON dari server Django (melalui http.get). View django yang berkaitan akan memproses permintaan dan memberikan data JSON. Setelah menerima data JSON, model Dart yang berkaitan akan melakukan parsing dan membuat list objek model dart. Saat data sudah dibuat, data tersebut akan ditampilkan oleh Widget yang berkaitan.

mekanisme register, login, logout flutter:
Register: mengisi field akun untuk registrasi. Widget mengconvert input ke JSON dan mengirim data ke url view autentikasi register (melalui http.post). View melakukan validasi berdasarkan data. Jika aman view akan membuat user baru. View lalu memberikan respons. Flutter lalu menampilkan tampilan berdasarkan respons server.

Login: mengisi field akun untuk login. Widget mengconvert input ke JSON dan mengirim data ke url view autentikasi login. View melakukan validasi login berdasarkan data. Jika berhasil login, server akan mengirimkan respons beserta cookie sessionid ke flutter. Flutter lalu menyimpan sessionid sebagai cookie dan melakukan navigasi ke menu yang sesuai.

Logout: melakukan permintaan logout (biasanya melalui tombol logout). Flutter akan melakukan http.post ke url logout dan juga mengirim cookie sessionid. View Django akan memproses logout dan memberikan respons. Setelah respons diterima, app flutter menghapus cookie sessionid nya.

Cara saya mengimplementasikan checklist:
- Membuat app autentikasi (untuk autentikasi flutter) di projek Django.
- Membuat view untuk melakukan registrasi, login, dan logout di app autentikasi flutter - dan melakukan routing url
- Membuat widget untuk autentikasi di flutter (yang mengintegrasikan app autentikasi Django).
- Mengubah homepage menjadi LoginPage().
- Menambahkan view django untuk memberi JSON product user.
- Membuat widget list product
- Membuat view untuk add product dari aplikasi flutter
- Melink widget form product ke django
- Menambah tombol logout

</details>
----------------------------------------------------------------------------------------------------------------------------------
<details>
<summary>Tugas 6</summary>
Perbedaan dari synchronus request dan asynchronus request adalah untuk synchronus request, setelah client memberikan request, client harus menunggu response dari server sebelum melakukan hal lainnya. Sementara untuk asynchronus request, client dapat melakukan hal lain tanpa perlu menunggu response dari server.

AJAX bekerja dalam django melalui tahapan berikut:
1. Terjadi event dari client.
2. JavaScript melakukan request HTTP ke suatu URL di Django server.
3. Melalui url tersebut, dipilih view yang sesuai dan menjalan fungsinya. Hasil biasanya dalam bentuk JsonResponse
4. Response yang diberikan diproses kode JavaScript dan memberikan hasil yang sesuai ke client

Cara memastikan keamanan untuk fitur login dan register adalah dengan melakukan perlindungan dari Cross Site Request Forgery (CSRF) dan menggunakan CSRF Token. CSRF Token dapat didapatkan melalui kode JavaScript yang akan dikirim melalui headar untuk permintaan POST, PUT, atau DELETE.

AJAX dapat meningkatkan pengalaman user seperti tidak perlunya untuk melakukan refresh untuk menampilkan hal baru, app bisa menampilkan message tanpa melakukan reload, dan app juga dapat dibuat lebih interaktif untuk user.

</details>
---------------------------------------------------------------------------------------
<details>
<summary>Tugas 5</summary>
Urutan prioritas dari pengambilan CSS selector dari inline styles (style yang langsung di elemen htmlnya), lalu ID Selector, lalu class selector, dan terakhir element selector

Responsive design menjadi konsep yang penting karena sehingga design web menjadi sesuai dengan device yang dipakai user. Contoh dari web yang sudah menerapkan responsive design adalah youtube.com yang menyesuaikan design antara desktop dan mobile.

Border adalah batasan yang mengililingi content (dan padding jika ada). Cara menerapkan border adalah dengan menggunakan kata kunci border dalam styling css dan terdapat berberapa property border seperti border-with, border-style, border-color, dll. Padding merupakan besaran spacing antara content dengan border. Cara menerapkan padding adalah dengan kata kunci padding dan memiliki beberapa property seperti padding-top, padding-bottom, padding-right, padding-left. Margin adalah besaran spacing antara element satu sama lain. Cara menerapkan margin adalah dengan kata kunci margin dan memiliki beberapa property seperti margin-top, margin-right, margin-bottom, margin-left.

Grid and Flexbox adalah konsep untuk mengatur layout di CSS. Perbedaan dari Grid dan Flexbox adalah kegunaan utamanya, Grid berguna untuk mengatur layout web secara keseluruhan, sementara flexbox berguna untuk mengatur tata dari content-content di web. 

Langkah mengimplementasikan checklist:
1. Membuat fungsi untuk delete dan edit produk di views.py dan templatenya.
2. Melink fungsi diatas di urls.py main
3. Menambah navigation bar template di template root.
4. Menambahkan tailwind dan menkonfigurasikan tailwind dan css
5. Menambahkan custom styling di global.css
6. Melakukan styling di template-template yang berada di aplikasi main.
7. Menambahkan README.md
</details>
----------------------------------------------------------------------------------------------------------------------------------
<details>
<summary>Tugas 4</summary>
Django AuthenticationForm adalah built-in form dari django yang dibuat untuk keperluan login. Kelebihannya adalah AuthenticationForm memudahkan implementasi login karena disediakan form dengan field username dan password. Kekurangannya adalah Django AuthenticationForm cukup minimal dalam opsi login yang disediakan.

Autentikasi adalah proses untuk memverifikasi identitas seseorang sesuai dengan yang dinginkan, sementara Otorisasi adalah proses untuk menentukan apa saja hal yang bisa dilakukan dalam sistem oleh orang tertentu. Django mengimplementasikan autentikasi dan otorisasi melalui modul django.contrib.auth yang memberikan banyak hal yang dapat digunakan untuk mengautentikasi dan mengatur permission.

Kelebihan dari session dan cookies adalah lebih aman dalam penyimpanan state (karena state disimpan di server), memudahkan user dalam penggunaan app (tidak perlu autentikasi terus menerus), dan data antara user tidak akan bertabrakan (session terisolasi antara user). Kekurangan dari session dan cookies adalah user perlu mengaktifasi fitur cookies dalam browsernya agar bisa menyimpan cookies

Cookies memiliki risiko bahwa user bisa saja dicuri dan digunakan untuk merequest hal tanpa sepengetahuan user. Untuk mengatasi ini Django memiliki sistem protection yaitu sistem CSRF Protection untuk memverifikasi bahwa request dari user yang benar.

Cara saya implementasi checklist:
1. Membuat fungsi registrasi dan template untuk registrasi (register.html)
2. Membuat fungsi login & logout dan template untuk login (login.html)
3. Merestriksi fungsi show_main (Main page app) & show_product (Product Details) sehingga harus login terlebih dahulu
4. Mengimplementasi cookies untuk menentukan kapan user terakhir login.
5. Menghubungkan model Product dengan User (django built-in model) sehingga product bisa memiliki seller sesuai dan user bisa menjual produk juga.
</details>
----------------------------------------------------------------------------------------------------------------------------------
<details>
<summary>Tugas 3</summary>

Data Delivery penting karena jika ada keperluan untuk merubah platform, data yang tersimpan sebelumnya bisa digunakan kembali.

Menurut saya JSON lebih baik dari XML, karena penampilan data yang lebih mudah dilihat. Mungkin itu juga alasan mengapa JSON lebih populer dibandingkan dengan XML.

is_valid() digunakan untuk menvalidasi data yang disubmit ke dalam form. is_valid() penting agar data yang disubmit dalam form sesuai dengan yang diinginkan.

csrf_token diperlukan saat membuat form agar memastikan request form benar-benar dari user yang meminta. Jika tidak ada csrf_token dan ada user yang sudah login ke website dengan form tersbeut, penyerang (melalui website lain atau lain hal) dapat meminta request ke form tersebut sesuai keinginannya karena tidak ada verfikasi kembali.

Cara saya implementasi checklist:
1. Membuat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id di views.py main
2. Melakukan url routing untuk fungsi diatas di urls.py main
3. Membuat forms.py untuk form add product 
4. Menambah web pws ke CSRF_TRUSTED_ORIGINS
5. Membuat fungsi show_product dan add_product di views.py main
6. Membuat folder template di root projek dan menambah base.html untuk template-template di main
7. Membuat template add_product.html dan product_detail.html
8. Merubah main.html sehingga tampilan sesuai dengan yang diinginkan
9. Menambah README.md

link folder foto screenshot postman: https://drive.google.com/drive/folders/1IVrW576fyTT00hWzBjCAtTKeyZuuHjeN?usp=drive_link
</details>
----------------------------------------------------------------------------------------------------------------------------
<details>
<summary>Tugas 2</summary>

Cara saya implementasi checklist:

Commit 1:
1. Membuat direktori projek dan inisiasi git (git init)
2. Membuat python virtual enviroment (python -m venv env, env nama folder virtual enviromentnya)
3. Mendownload requirements untuk projeknya (ada di requirements.txt)
4. Membuat projek Django (django startproject all_football_shop .)
5. Mengkonfigurasi enviroment variables

Commit 2:
1. Buat projek di PWS
2. Link git projek ke pws

Commit 3:
1. Membuat models.py berdasarkan yang diminta
2. Membuat template untuk tampilan web
3. Membuat views.py yang akan merender web
4. Menkofigurasi urls.py pada aplikasi main
5. Menkofigurasi urls.py projek django (agar menggunakan urls.py main)
6. Membuat README.md

Link Bagan: https://www.canva.com/design/DAGyRYkC77c/Ti4qF2BbM8QuzdsWf7XaAw/edit?utm_content=DAGyRYkC77c&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

settings.py berguna untuk menkonfigurasi semua hal di projek django yang dibuat.

Melakukan migration untuk perubahan model dapat dilakukan dengan:
1. Menjalankan python manage.py makemigration melalui terminal di folder projek 
2. Menjalankan python manage.py migrate untuk melakukan migration

Django dijadikan permulaan pembelajaran pengembangan proyek lunak mungkin karena menggunakaan bahasa yang cukup mudah (Python) serta banyak hal yang diperlukan untuk web app langsung disediakan oleh Django.

Menurut saya tutorial 1 sudah cukup mudah untuk diikuti jalan prosesnya.
</details>