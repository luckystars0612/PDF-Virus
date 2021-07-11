from PyPDF4 import PdfFileWriter, PdfFileReader

import optparse

def Main():
    """add-js-to-pdf, use it to add embedded JavaScript to a PDF document that will execute automatically when the document is opened
    """

    parser = optparse.OptionParser(usage='usage: %prog [options] in-pdf-file out-pdf-file', version='%prog 0.1')
    parser.add_option('-j', '--javascript', help='javascript to embed (default embedded JavaScript is app.alert messagebox)')
    parser.add_option('-f', '--javascriptfile', help='javascript file to embed')
    (options, args) = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        print ''
        print '  add-js-to-pdf, use it to add embedded JavaScript to a PDF document that will execute automatically when the document is opened'
        print '  Based on modified pyPDF http://pybrary.net/pyPdf/ and inspiration from https://DidierStevens.com'
        print ''
        return

    input1 = PdfFileReader(file(args[0], "rb"))
    output = PdfFileWriter()
        
    pages = input1.getNumPages()
    for p in range(pages):
        output.addPage(input1.getPage(p))
    if options.javascript == None and options.javascriptfile == None:
            javascript = """app.alert({cMsg: 'Hello from PDF JavaScript', cTitle: 'Testing PDF JavaScript', nIcon: 3});"""
    elif options.javascript != None:
            javascript = options.javascript
    else:
        try:
            fileJavasScript = open(options.javascriptfile, 'rb')
        except:
            print "error opening file %s" % options.javascriptfile
            return

        try:
            javascript = fileJavasScript.read()
        except:
            print "error reading file %s" % options.javascriptfile
            return
        finally:
            fileJavasScript.close()

    output.addJS(javascript)
    outputStream = file(args[1], "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ == '__main__':
    Main()
