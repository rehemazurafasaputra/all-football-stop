Link ke PWS = https://rehema-zurafa-allfootballstop.pbp.cs.ui.ac.id/

Tugas 2:

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
----------------------------------------------------------------------------------------------------------------------------
Tugas 1:

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


