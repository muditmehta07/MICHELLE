<!DOCTYPE html>
<html style="background: rgba(0, 5, 19, 0.918); background-image: url(./imgs/main-bg.jpg);" >
<title>Home</title>
<link rel="icon" href="./imgs/icon.png">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>
        body {
          margin: 0;
          font-family: Arial, Helvetica, sans-serif;
        }

        footer {
          position: fixed;
          bottom: 0;
          left: 0;
          width: 100% ;
          overflow: hidden;
          background-color: rgba(0, 0, 0, 0.800);
        }

        footer a {
          float: left;
          color: #c8c8c8;
          text-align: center;
          padding: 14px 16px;
          text-decoration: none;
          font-size: 17px;
        }

        footer a:hover {
          background-color: rgba(221, 221, 221, 0.75);
          color: black;
        }
        
        footer a.active {
          background-color: #00adadce;
          color: #00adad;
        }
        
        .topnav {
          position: fixed;
          top: 0;
          width: 100%;
          overflow: hidden;
          background-color: rgba(0, 0, 0, 0.800);
        }
        
        .topnav a {
          display: block;
          float: left;
          color: #c8c8c8;
          text-align: center;
          padding: 14px 16px;
          text-decoration: none;
          font-size: 17px;
        }
        
        .topnav a:hover {
          background-color: rgba(221, 221, 221, 0.75);
          color: black;
        }
        
        .topnav a.active {
          background-color: #00adadce;
          color: white;
        }

        .topnav .icon {
          display: none;
        }

        .intro {
          margin-top: 12%;
          margin-bottom: 10%;
          text-align: center;
          font-family: Arial, Helvetica, sans-serif;
          color: aliceblue;
          padding: 2%;
        }

        @media screen and (max-width: 600px) {
          .topnav a:not(:first-child) {display: none;}
          .topnav a.icon {
            float: right;
            display: block;
          }
        }

        @media screen and (max-width: 600px) {
          .topnav.responsive {position: fixed;}
          .topnav.responsive .icon {
            position: absolute;
            right: 0;
            top: 0;
          }

          .topnav.responsive a {
            float: none;
            display: block;
            text-align: left;
          }
        }

        button[type=invite] {
          width: 100px;
          color: white;
          font-size: large;
          background-color: #00adad;
          padding: 14px 20px;
          margin: 15px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }

        button[type=invite]:hover {
          color: black;
          background-color: #00f3cb;
        }

        button[type=join] {
          width: 110px;
          color: white;
          font-size: large;
          background-color: #00adad;
          padding: 14px 20px;
          margin: 15px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }

        button[type=join]:hover {
          color: black;
          background-color: #00f3cb;
        }
        </style>
        
        <div class="topnav" id="myTopnav">
          <a class="active" href="./index.html">Home</a>
          <a href="./commands.html">Commands</a>
          <a href="./patch.html">Patch Notes</a>
          <a href="./staff.html">Staff</a>
          <a href="https://github.com/MuditMehta07/Michelle">GitHub</a>
          <a href="javascript:void(0);" class="icon" onclick="myFunction()">
            <i class="fa fa-bars"></i>
          </a>
        </div>

        <script>
          function myFunction() {
            var x = document.getElementById("myTopnav");
            if (x.className === "topnav") {
              x.className += " responsive";
            } else {
              x.className = "topnav";
            }
          }
        </script>

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body>
      <div class="intro">
        <img src="https://cdn.discordapp.com/avatars/840180379389263882/86accdc6935870ec59ca8c53d4679f62.webp?size=1024" style="width: 125px; border-radius: 50%;">
        <p style="font-size: 50px;">MICHELLE</p>
        <p style="font-size: 20px; color: rgb(202, 202, 202);">A Multipurpose bot with a Leveling System, Economy, Fun commands and more</p>
        <a href="https://discord.com/oauth2/authorize?client_id=840180379389263882&permissions=8&scope=bot+applications.commands"><button type="invite">Invite</button></a>
        <a href="https://discord.gg/EfHrMURtnA"><button type="join">Server</button></a>
      </div>

      <footer>
        <a href="https://github.com/MuditMehta07/Michelle/blob/main/PrivacyPolicy.md">Privacy Policy</a>
        <a href="https://github.com/MuditMehta07/Michelle/blob/main/TermsOfService.md">Terms of Service</a>
        <a href="https://top.gg/bot/840180379389263882">Top.gg</a>
      </footer>

    </body>
</html>
