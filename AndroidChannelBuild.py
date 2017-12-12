#vim: set fileencoding:utf-8

__author__ = 'Jack'
import os
import sys
import shutil
import zipfile


#���ļ� ����д��˿��ļ���apk������Ϊchannel�ļ�
src_empty_file = 'info/info.txt'
f = open(src_empty_file, 'a')
f.close()

#��ȡ�����б�
channel_file = 'info/channels.txt'
f = open(channel_file)
lines = f.readlines();
f.close()

#��ȡ����APK�ļ�
# python3 : os.listdir()���ɣ�����ʹ�ü���Python2��os.listdir('.')
apk_path = os.listdir(".")
src_apks = []
for file in apk_path:
    if os.path.isfile(file):
		# �ָ��ļ������׺
        file_path, file_extension = os.path.splitext(file)
        if file_extension == '.apk':
            src_apks.append(file)

#���������Ų�д��apk
for src_apk in src_apks:
    src_apk_file_name = os.path.basename(src_apk)
	#��չ��Ϊapk
    src_apk_name, src_apk_extension = os.path.splitext(src_apk)
	#�������ɵĶ�����apk������
    output_dir = 'output_' + src_apk_name + '/'
	#Ŀ¼�������򴴽�
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for line in lines:
		# ��ȡ��ǰ�����ţ���Ϊ�������ļ��л�ô���\n,����stripһ��
        target_channel = line.strip()
		#ƴ�Ӷ�Ӧ�����ŵ�apk
        target_apk = output_dir + src_apk_name + "-" + target_channel + src_apk_extension
		#����Դapk��Ŀ��apk��
        shutil.copy(src_apk,  target_apk)
		#ѹ��
        zipped = zipfile.ZipFile(target_apk, 'a', zipfile.ZIP_DEFLATED)
		#��ʼ��������Ϣ
        empty_channel_file = "META-INF/channel_{channel}".format(channel=target_channel)
		#д��������Ϣ
        zipped.write(src_empty_file, empty_channel_file)
		#�ر�zip��
        zipped.close()