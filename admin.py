import urllib , sys , requests , os
from platform import system
from time import sleep

adminlist = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/', 'memberadmin/', 'administratorlogin/', 'adm/', 'account.asp', 'admin/account.asp', 'admin/index.asp', 'admin/login.asp', 'admin/admin.asp', 'admin_area/admin.asp', 'admin_area/login.asp', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html', 'admin_area/admin.html', 'admin_area/login.html', 'admin_area/index.html', 'admin_area/index.asp', 'bb-admin/index.asp', 'bb-admin/login.asp', 'bb-admin/admin.asp', 'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html', 'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'administrator/index.html', 'administrator/login.html', 'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator.html', 'moderator/login.html', 'moderator/admin.html', 'account.html', 'controlpanel.html', 'admincontrol.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/home.asp', 'admin/controlpanel.asp', 'admin.asp', 'pages/admin/admin-login.asp', 'admin/admin-login.asp', 'admin-login.asp', 'admin/cp.asp', 'cp.asp', 'administrator/account.asp', 'administrator.asp', 'acceso.asp', 'login.asp', 'modelsearch/login.asp', 'moderator.asp', 'moderator/login.asp', 'administrator/login.asp', 'moderator/admin.asp', 'controlpanel.asp', 'adminpanel.html', 'webadmin.html', 'pages/admin/admin-login.html', 'admin/admin-login.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'user.asp', 'user.html', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html', 'admin/adminLogin.html', 'adminLogin.html', 'home.html', 'adminarea/index.html', 'adminarea/admin.html', 'adminarea/login.html', 'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html', 'admin/admin_login.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'admincontrol.asp', 'adminpanel.asp', 'webadmin.asp', 'webadmin/index.asp', 'webadmin/admin.asp', 'webadmin/login.asp', 'admin/admin_login.asp', 'admin_login.asp', 'panel-administracion/login.asp', 'adminLogin.asp', 'admin/adminLogin.asp', 'home.asp', 'adminarea/index.asp', 'adminarea/admin.asp', 'adminarea/login.asp', 'admin-login.html', 'panel-administracion/index.asp', 'panel-administracion/admin.asp', 'modelsearch/index.asp', 'modelsearch/admin.asp', 'administrator/index.asp', 'admincontrol/login.asp', 'adm/admloginuser.asp', 'admloginuser.asp', 'admin2.asp', 'admin2/login.asp', 'admin2/index.asp', 'adm/index.asp', 'adm.asp', 'affiliate.asp', 'adm_auth.asp', 'memberadmin.asp', 'administratorlogin.asp', 'siteadmin/login.asp', 'siteadmin/index.asp', 'siteadmin/login.htmladmin/', 'usuarios/', 'usuario/', 'admin/account.php', 'admin/index.php', 'admin/login.php', 'admin/admin.php', 'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 'siteadmin/index.php', 'siteadmin/login.html', 'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php', 'admin/home.php', 'admin/controlpanel.php', 'admin.php', 'admin/cp.php', 'cp.php', 'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php', 'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php', 'administrator/account.php', 'administrator.php', 'pages/admin/admin-login.php', 'admin/admin-login.php', 'admin-login.php', 'acceso.php', 'login.php', 'modelsearch/login.php', 'moderator.php', 'moderator/login.php', 'moderator/admin.php', 'account.php', 'controlpanel.php', 'admincontrol.php', 'rcjakar/admin/login.php', 'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'adminpanel.php', 'user.php', 'panel-administracion/login.php', 'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php', 'adminarea/index.php', 'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php', 'panel-administracion/admin.php', 'modelsearch/index.php', 'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php', 'admin2.php', 'admin2/login.php', 'admin2/index.php', 'usuarios/login.php', 'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php', 'administratorlogin.php', 'admin/account.cfm', 'admin/index.cfm', 'admin/login.cfm', 'admin/admin.cfm', 'admin_area/admin.cfm', 'admin_area/login.cfm', 'siteadmin/login.cfm', 'siteadmin/index.cfm', 'admin_area/index.cfm', 'bb-admin/index.cfm', 'bb-admin/login.cfm', 'bb-admin/admin.cfm', 'admin/home.cfm', 'admin/controlpanel.cfm', 'admin.cfm', 'admin/cp.cfm', 'cp.cfm', 'administrator/index.cfm', 'administrator/login.cfm', 'nsw/admin/login.cfm', 'webadmin/login.cfm', 'admin/admin_login.cfm', 'admin_login.cfm', 'administrator/account.cfm', 'administrator.cfm', 'pages/admin/admin-login.cfm', 'admin/admin-login.cfm', 'admin-login.cfm', 'login.cfm', 'modelsearch/login.cfm', 'moderator.cfm', 'moderator/login.cfm', 'moderator/admin.cfm', 'account.cfm', 'controlpanel.cfm', 'admincontrol.cfm', 'acceso.cfm', 'rcjakar/admin/login.cfm', 'webadmin.cfm', 'webadmin/index.cfm', 'webadmin/admin.cfm', 'adminpanel.cfm', 'user.cfm', 'panel-administracion/login.cfm', 'wp-login.cfm', 'adminLogin.cfm', 'admin/adminLogin.cfm', 'home.cfm', 'adminarea/index.cfm', 'adminarea/admin.cfm', 'adminarea/login.cfm', 'panel-administracion/index.cfm', 'panel-administracion/admin.cfm', 'modelsearch/index.cfm', 'modelsearch/admin.cfm', 'admincontrol/login.cfm', 'adm/admloginuser.cfm', 'admloginuser.cfm', 'admin2.cfm', 'admin2/login.cfm', 'admin2/index.cfm', 'usuarios/login.cfm', 'adm/index.cfm', 'adm.cfm', 'affiliate.cfm', 'adm_auth.cfm', 'memberadmin.cfm', 'administratorlogin.cfm', 'admin/account.js', 'admin/index.js', 'admin/login.js', 'admin/admin.js', 'admin_area/admin.js', 'admin_area/login.js', 'siteadmin/login.js', 'siteadmin/index.js', 'admin_area/index.js', 'bb-admin/index.js', 'bb-admin/login.js', 'bb-admin/admin.js', 'admin/home.js', 'admin/controlpanel.js', 'admin.js', 'admin/cp.js', 'cp.js', 'administrator/index.js', 'administrator/login.js', 'nsw/admin/login.js', 'webadmin/login.js', 'admin/admin_login.js', 'admin_login.js', 'administrator/account.js', 'administrator.js', 'pages/admin/admin-login.js', 'admin/admin-login.js', 'admin-login.js', 'login.js', 'modelsearch/login.js', 'moderator.js', 'moderator/login.js', 'moderator/admin.js', 'account.js', 'controlpanel.js', 'admincontrol.js', 'rcjakar/admin/login.js', 'webadmin.js', 'webadmin/index.js', 'acceso.js', 'webadmin/admin.js', 'adminpanel.js', 'user.js', 'panel-administracion/login.js', 'wp-login.js', 'adminLogin.js', 'admin/adminLogin.js', 'home.js', 'adminarea/index.js', 'adminarea/admin.js', 'adminarea/login.js', 'panel-administracion/index.js', 'panel-administracion/admin.js', 'modelsearch/index.js', 'modelsearch/admin.js', 'admincontrol/login.js', 'adm/admloginuser.js', 'admloginuser.js', 'admin2.js', 'admin2/login.js', 'admin2/index.js', 'usuarios/login.js', 'adm/index.js', 'adm.js', 'affiliate.js', 'adm_auth.js', 'memberadmin.js', 'administratorlogin.js', 'admin/account.cgi', 'admin/index.cgi', 'admin/login.cgi', 'admin/admin.cgi', 'admin_area/admin.cgi', 'admin_area/login.cgi', 'siteadmin/login.cgi', 'siteadmin/index.cgi', 'admin_area/index.cgi', 'bb-admin/index.cgi', 'bb-admin/login.cgi', 'bb-admin/admin.cgi', 'admin/home.cgi', 'admin/controlpanel.cgi', 'admin.cgi', 'admin/cp.cgi', 'cp.cgi', 'administrator/index.cgi', 'administrator/login.cgi', 'nsw/admin/login.cgi', 'webadmin/login.cgi', 'admin/admin_login.cgi', 'admin_login.cgi', 'administrator/account.cgi', 'administrator.cgi', 'pages/admin/admin-login.cgi', 'admin/admin-login.cgi', 'admin-login.cgi', 'login.cgi', 'modelsearch/login.cgi', 'moderator.cgi', 'moderator/login.cgi', 'moderator/admin.cgi', 'account.cgi', 'controlpanel.cgi', 'admincontrol.cgi', 'rcjakar/admin/login.cgi', 'webadmin.cgi', 'webadmin/index.cgi', 'acceso.cgi', 'webadmin/admin.cgi', 'adminpanel.cgi', 'user.cgi', 'panel-administracion/login.cgi', 'wp-login.cgi', 'adminLogin.cgi', 'admin/adminLogin.cgi', 'home.cgi', 'adminarea/index.cgi', 'adminarea/admin.cgi', 'adminarea/login.cgi', 'panel-administracion/index.cgi', 'panel-administracion/admin.cgi', 'modelsearch/index.cgi', 'modelsearch/admin.cgi', 'admincontrol/login.cgi', 'adm/admloginuser.cgi', 'admloginuser.cgi', 'admin2.cgi', 'admin2/login.cgi', 'admin2/index.cgi', 'usuarios/login.cgi', 'adm/index.cgi', 'adm.cgi', 'affiliate.cgi', 'adm_auth.cgi', 'memberadmin.cgi', 'administratorlogin.cgi', 'admin/account.brf', 'admin/index.brf', 'admin/login.brf', 'admin/admin.brf', 'admin_area/admin.brf', 'admin_area/login.brf', 'siteadmin/login.brf', 'siteadmin/index.brf', 'admin_area/index.brf', 'bb-admin/index.brf', 'bb-admin/login.brf', 'bb-admin/admin.brf', 'admin/home.brf', 'admin/controlpanel.brf', 'admin.brf', 'admin/cp.brf', 'cp.brf', 'administrator/index.brf', 'administrator/login.brf', 'nsw/admin/login.brf', 'webadmin/login.brfbrf', 'admin/admin_login.brf', 'admin_login.brf', 'administrator/account.brf', 'administrator.brf', 'acceso.brf', 'pages/admin/admin-login.brf', 'admin/admin-login.brf', 'admin-login.brf', 'login.brf', 'modelsearch/login.brf', 'moderator.brf', 'moderator/login.brf', 'moderator/admin.brf', 'account.brf', 'controlpanel.brf', 'admincontrol.brf', 'rcjakar/admin/login.brf', 'webadmin.brf', 'webadmin/index.brf', 'webadmin/admin.brf', 'adminpanel.brf', 'user.brf', 'panel-administracion/login.brf', 'wp-login.brf', 'adminLogin.brf', 'admin/adminLogin.brf', 'home.brf', 'adminarea/index.brf', 'adminarea/admin.brf', 'adminarea/login.brf', 'panel-administracion/index.brf', 'panel-administracion/admin.brf', 'modelsearch/index.brf', 'modelsearch/admin.brf', 'admincontrol/login.brf', 'adm/admloginuser.brf', 'admloginuser.brf', 'admin2.brf', 'admin2/login.brf', 'admin2/index.brf', 'usuarios/login.brf', 'adm/index.brf', 'adm.brf', 'affiliate.brf', 'adm_auth.brf', 'memberadmin.brf', 'administratorlogin.brf']
def clear():
	if os.name =="posix" or os.name == "Linux":
		os.system('clear')
	elif system=="Windows":
		os.system('cls')
logo = '''

   ______          __        
  / __/ /__ __ _  / /__ __ _    
 _\ \/  '_//  ' \/  '_//  ' \  Title  : admin panel finder
/___/_/\_\/_/_/_/_/\_\/_/_/_/  Author : Skmkm - EBF hackers
			       							

'''
clear()
fin="\033[1;m"
BLUE="\033[1;34m"
RED="\033[1;31m"
GREEN="\033[1;32m"
GRAY = "\033[1;30m"
print(logo)

def trying():
 try:		
	
	
	site = sys.argv[1]
	if not site.startswith("http://") or site.startswith("https://"):
		site = "http://"+site
	if not site.endswith("/"):
		site= site+"/"
	for admin in adminlist:			
	
		get_url=requests.get(site+admin)		
		print GRAY+'Please wait ..'
		if get_url.status_code == 200:
			print BLUE+" [+] Success ==>"+fin+GREEN,"[",get_url.status_code,"]",site+admin+fin+"\n"
			sys.exit()
		elif get_url.status_code != 200:
			print RED+" [ ! ] Failed ="+fin+GRAY,"[",get_url.status_code,"]",site+admin+fin+"\n"

 except IndexError as e:
	for char in RED+'\n\t\t{+} Correct Usage :'+BLUE+' python '+sys.argv[0]+RED+' http://'+BLUE+'example.com'+RED+'/\n\n'+fin:
		sys.stdout.write(char)
		sys.stdout.flush()
		sleep(0.05)
 except KeyboardInterrupt:

    exit =  raw_input(RED+"\n\tAre You sure You want to exit ? : "+fin)	
    if exit in ['yes', 'Yes','y','Y','ye','YES','yees']:
		print GREEN+'\n\t\tExiting ... '   
 		sys.exit()
    else:
	trying()
trying()

		
