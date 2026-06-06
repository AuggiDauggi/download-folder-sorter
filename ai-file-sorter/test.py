text = read_pdf(file)

category = classify(text)

move_file(file, category)
