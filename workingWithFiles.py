#если путь не указан идет текстовый файл в проект
#надо указать путь для файла после какой файл нужен
#к примеру пусть - /Users/imac/Desktop/newfolderforpythonproject/



#'r' для чтения
#'t' открыть в текстовым режиме
#'w' открыть для записи , содержимое удалаеться ,  если нет файла создаеться новый
#'a' открыть для дозаписи в конец файла если нет создаеться новый
#'b' открыть в бинарном режиме
#'+' открыть для чтение и записи 'r+' , 'w+' , 'a+'



r = open('text2.txt' , 'w' , encoding='utf-8')
print(r.write('stroke text'))


r.close()