#EmreZeriX Tarafından Python3 Kullanılarak Deneysel Olarak Yazılmıştır

import os # Os Modülü sistem komutlaını çalıştırır.
#EmreZeriX
os.system('clear') #os modülü ile ekranı temizledim
print(''' ____  __  __ ____      _____ _____ ____  ____ ___ _____    
/ ___||  \/  | __ )    |_   _| ____/ ___||  _ \_ _|_   _|
\___ \| |\/| |  _ \ _____| | |  _| \___ \| |_) | |  | |  
 ___) | |  | | |_) |_____| | | |___ ___) |  __/| |  | |  
|____/|_|  |_|____/      |_| |_____|____/|_|  |___| |_|  
                                                         
''''') #''''''' tırnakları ile python da alt alta yazmaktan kurtuldum!
print('=========================================================')
print('Smb servisine yönelik güvenlik açığı analizi yapmaktadır!')
print('=========================================================')

print('[1]-Smb brute force denetimi')
print('[2]-Sistem Bilgisi')
print('[3]-MS17-010 Zafiyet tespiti')
print('[4]-Paylaşılan ortak dizin tespiti') #EmreZeriX
print('[5]-Kullanıcı adı tespiti')
print('[6]-Backdoor Kontrolü')
print('[7]-Çıkış')
print('=========================================================')


while(True):
	a = input('İşlem Numarası : ') # a değişkenini input aldık
	if(a=='1'):
		print('')
		print('Smb brute force : smb portuna kaba kuvvet saldırısı yapılabilir mi onu denetler!')
		print('')
		b = input('Hedef Site : ')
		print('')
		os.system('nmap {0} --script smb-brute -p139,445'.format(b))
	if(a=='2'):
		print('')
		print('System Bilgisi : Hedef Sistem bilgisini elde etmeye çalışır.')
		print('')
		b = input('Hedef Site : ')
		print('')
		os.system('nmap {0} --script smb-system-info -p139,445'.format(b))
	if(a=='3'):
		print('')
		print('MS17-010 : Güvenlik açığının olup olmadığını kontrol eder.')
		print('')
		b = input('Hedef Site : ')
		print('==========================================================')
		os.system('nmap {0} --script smb-vuln-ms17-010 -p139,445'.format(b))
	if(a=='4'):
		print('')
		print('Enum Shares : Paylaşılan dizinleri tespit etmeye çalışır.')
		print('')
		b = input('Hedef Site : ')
		print('')
		os.system('nmap {0} --script smb-enum-shares -p139,445'.format(b))
	if(a=='5'):
		print('======================================================')
		print('Enum Users : Kullanıcı adlarını tespit etmeye çalışır.')
		print('======================================================')
		b = input('Hedef Site : ')
		print('======================================================')
		os.system('nmap {0} --script smb-enum-users -p139,445'.format(b))
	if(a=='6'):
		print('==============================================')
		print('Backdoor Kontrolü : Backdoor kontrolünü yapar.')
		print('==============================================')
		b = input('Hedef Site : ')
		print('==============================================')
		os.system('nmap {0} --script smb-double-pulsar-backdoor -p139,445'.format(b))
	if(a=='7'):
		print('Çıkış yapılıyor...')
		break
	else:
		print('Hatalı işlem numarası girdiniz!')
		os.system('python3 smbtespit.py')
