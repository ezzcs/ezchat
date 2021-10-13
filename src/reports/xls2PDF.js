module.paths.push("/usr/local/lib/node_modules");

var toPdf = require("office-to-pdf");

var fs = require('fs');

// 转换word为PDF

function wordToPdf(){
  //let wordFile = "./2.ods";
  let wordFile = "./3.xls";

  console.log(53,wordFile)

  return fs.readFile(wordFile, function(err, result){
    console.log(55,result)

    if(err){
      console.log(err);

    }else{
      toPdf(result).then(

        (pdfBuffer) => {
          console.log(60,pdfBuffer)

          fs.writeFileSync("./2.pdf", pdfBuffer);

          console.log('成功生成PDF文件')

          // sendFileToServer('./pdf/test.pdf' , '/sftp/pdf/test.pdf')

        }, (err) => {
          console.log(66,err);

        }

      );

    }

  });

}

wordToPdf();
