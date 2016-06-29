#!/bin/bash
printf "Content-Type: text/html\n\n"
printf '<!DOCTYPE html>
<html class=" js mozilla"><head>
<title>Own-Mailbox setup.</title>
<meta name="Robots" content="noindex,nofollow">
<meta http-equiv="X-UA-Compatible" content="IE=EDGE">
<meta name="viewport" content="" id="viewport">
<link rel="stylesheet" type="text/css" href="../first/files/styles.css">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">';

attempt=$(cat /tmp/attempt_www)
if [ "$attempt" = "" ]; then
  attempt="1";
else
  attempt=$((attempt+1))
fi

torsocks wget --timeout $((attempt+1+attempt)) http://proxy.omb.one/OK -O /tmp/ok_www > /dev/null 2>&1
res_wget=$?;
hostname=$(sudo /bin/cat /var/lib/tor/omb_hidden_service/hostname);
res_cat=$?;

echo "$attempt"> /tmp/attempt_www

if [ "$res_wget" -eq "0" ] && [ "$res_cat" -eq "0" ] && [ "$hostname" != "" ]; then
 printf '<meta http-equiv="refresh" content="0; URL=../first/03-Identification-cookie.html">'
else
 printf '<meta http-equiv="refresh" content="'
 printf "$((attempt+5+attempt))"
 printf '; URL=">'
fi

printf "        
    <script>       
    function handleHideFAQ() {
    var div = document.getElementById('FAQsection10');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
    }
    };
    </script>"
    
printf '</head>
<body>

<img src="../first/files/images/logo.png"></img>
<div id="login-form"  >
<div class="box-inner" style="width:480px; height:300px;">

<center>

<div id="i_waiting" style="position : fixed; width : 420px;">
<p>
<font color="white" size="6" style="	text-shadow: 2px 2px #000000;">Connecting to the tor network.</font></br>
<font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Please wait...</font></br>
</p>
<div style="height:250px"></div>
<p>
<ul class="loader">
  <li>
    <div class="circle"></div>
    <div class="ball"></div>
  </li>
  <li>
    <div class="circle"></div>
    <div class="ball"></div>
  </li>
  <li>
    <div class="circle"></div>
    <div class="ball"></div>
  </li>
  <li>
    <div class="circle"></div>
    <div class="ball"></div>
  </li>
  <li>
    <div class="circle"></div>
    <div class="ball"></div>
  </li>
</ul>
</p>
</div>

</div>
<div  style="height:100px;"></div>

<div class="box-inner" style="width:480px; height:200px;">

<div align="left">
  <a onclick="handleHideFAQ();" style="display:visible"><font color="grey" size="4" style="	text-shadow: 2px 2px #000000;">&#10140;Connection logs.</font></a>
		 <div style="height:25px"></div>
		 <div id="FAQsection10" style="display:none">                   
               <textarea rows="5" cols="55">'
cat /var/log/tor.log;    
printf '</textarea>               </div>
</div>  

</center>
   <div style="height:25px"></div>

</body></html>';
 
 
