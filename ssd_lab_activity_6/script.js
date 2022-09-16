//const element = document.getElementById("smbt");
//element.addEventListener("click", submitHandler);
//document.getElementById("cspwd").addEventListener("blur", checkPwd);

function submitHandler()
{
    var mgrName = document.getElementById('mgr').value.trim();
    var grpEmail = document.getElementById('emailid').value.trim();
    var serverName = document.getElementById('suname').value.trim();
    var serverPwd1 = document.getElementById('spwd').value;
    var serverPwd2 = document.getElementById('cspwd').value;
    var teamLead = document.getElementById('lead').value;
    if( mgrName.length == 0 || grpEmail.length == 0 || serverName.length == 0 || serverPwd1.length == 0 || serverPwd2.length == 0 || teamLead.length == 0 || checkSName())
    {
        alert("Errors in form");
        return;
    }
    alert("Name : " + mgrName + "\n" + "Email : " + grpEmail + "\n" + "Username : " + serverName + "\n" + "Team Lead : " + teamLead + "\n" + "Team Members : ");
}

function checkPwd()
{
    var x = document.getElementById('spwd').value;
    var y = document.getElementById('cspwd').value;
    if( x != y )
    {
        alert("Passwords do not match");
    }
}

function checkEmail()
{
    var eid = document.getElementById('emailid').value;
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(eid))
    {
        document.getElementById('errorEmail').innerHTML="";
        return true;
    }
    else
    {
        //alert("invalid email");
        document.getElementById('errorEmail').innerHTML="Invalid Email ID";
        return false;
    }
}

function checkSName()
{
    var serverName = document.getElementById('suname').value.trim();
    if( /^(?=.*[A-Z])(?=.*\\d).+$/.test(serverName) )
    {
        document.getElementById('errorName').innerHTML="";
        return false;
    }
    else
    {
        document.getElementById('errorName').innerHTML="Invalid Server Name";
        return true;
    }
}