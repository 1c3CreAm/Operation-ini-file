方便操作INI文件的python库


读取ini：
read_ini(ini_path)                             #ini_path：文件位置

修改ini：
modify_ini(main_name,term_name,a)              #main_name:主项名称、term_name:分项名称、a:准备修改的值

写入ini（如果有需求）：
write_ini(ini_path,modify_result)              #modify_result：modify_ini方法得到的结果
