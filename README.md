Link ke PWS = https://rehema-zurafa-allfootballstop.pbp.cs.ui.ac.id/
<details>
<summary>Tugas 4</summary>
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
<summary>Tugas 3</summary>
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
<summary>Tugas 2</summary>

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
<summary>Tugas 1:</summary>

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