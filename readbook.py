# carga el documento en memoria.
def load_doc(filename):
 # abre el archivo como de solo lectura.
 file = open(filename, mode='rt', encoding='utf-8')
 # lee todo el texto.
 text = file.read()
 # cierra el archivo.
 file.close()
 return text


# divide el documento cargado en líneas.
def to_lines(doc):
 lines = doc.strip().split('\n')
 return lines


# muestra una línea.
def format_text(line):
 line_length = 96
 while len(line)>line_length:
  pos = line.find(" ",line_length)
  if pos!=-1:
   print(line[0:pos])
   line=line[(pos+1):]
  else:
   line=""
 print(line)


# muestra el contenido.
def show_text(line):
 texts = line.strip().split('\n')
 for text in texts:
  format_text(text)


# obtiene las opciones y muestra la página.
def get_options(lines, page_number):
 join_pages = True
 show = False

 content = ""
 options = []
 for line in lines:
  pos = line.find("*página")
  if pos!=-1:
   pageLine = line.replace("*página ", "")
   show = (str(page_number) == str(pageLine))
  else:
   if show:
    if line.find("a la página") != -1:
     options.append(line)
    else:
     if line == "Fin":
      options.append(line)
     else:
      if len(line) > 0:
       line += "\n"
      content += line
 if join_pages:
  if len(options)==1:
   if options[0]!="Fin":
    new_content, options = get_options(lines, get_page_number(options[0]))
    content = content + "* * * *\n" + new_content
 return content, options


# obtiene la página a la que hace referencia una opción.
def get_page_number(line):
 result = ""
 text = "a la página "
 pos = line.find(text)
 if pos != -1:
  result = line[pos + len(text):].replace(".", "")
 return result


# juega con el libro.
def play(lines):
 page_number = "1"
 stop_game = False
 while not stop_game:
  content, options = get_options(lines, page_number)
  print('* * * *\n* * * *\n* * * *')
  show_text(content)
  for i in range(0, len(options)):
   format_text(str(i + 1) + " > > > " + options[i])
  selected = input()
  if selected == "stop":
   stop_game = True
  # si la opción seleccionada no es válida, vuelve a preguntarla.
  while (int(selected) < 0) or (int(selected) > len(options)):
   print("- - - ¡Opción no válida!")
   selected = input()
  if len(options) > 0:
   option = options[int(selected) - 1]
   if option == "Fin":
    page_number = 1
   else:
    page_number = get_page_number(option)
  else:
   print("<!> ¡SIN OPCIONES!")
   stop_game = True

# carga el libro.
filename = 'aventura.txt'

doc = load_doc(filename)

# divide el libro en líneas.
lines = to_lines(doc)

#juega con el libro
play(lines) 
