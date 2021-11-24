try{
    p = document.querySelectorAll('a[onclick="opneinstahelp();"]')
    for (i = 0; i <= p.length; i++) { 
        p[i].setAttribute("onclick","javascrip:document.getElementById('allincall-popup-minimized-icon').click()")
    }
}catch(e){}