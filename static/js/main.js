var player = {};
var alien = {};
var foo = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
var pressed = 0;
var secondsPassed = 0;
var collisionOccured = false;
var saved_high_score = false;

console.log('foo is ' + foo);
player[foo] = new Player(10, 10, 10);
alien[foo] = new Alien(500, 50, 50);

// set key movements to false, when true, the ship moves.
var keyW = false;
var keyA = false;
var keyS = false;
var keyD = false;
var spacebar = false;

// This snippet is provided in Django official documentation
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


window.onload = function(){
if(document.querySelector("#authenticated").textContent == 'yes') {

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

// scene.add( player.createBox );
scene.add( player[foo].cube );

scene.add( alien[foo].cube );

camera.position.z = 5;

document.addEventListener('keydown', (event) => {
  const keyCode = event.keyCode;
  if(collisionOccured == false) {
    document.onkeyup = player[foo].movePlayer1(keyCode, pressed);
  }
  pressed = 1;
});

  setInterval(function(){
    if(collisionOccured == false) {
      secondsPassed = secondsPassed + 1;
    }
    if(collisionOccured == false) {
      document.querySelector("#game-clock").textContent = secondsPassed;
    }
  }, 1000);


var animate = function () {
  if(collisionOccured == false) {
    player[foo].updatePlayer();
    alien[foo].updateAlien();
  }
  if(player[foo].collision(alien[foo]) && saved_high_score == false) {
    var audio = new Audio('static/audio/pickup.wav');
    audio.play();
    console.log('collision');
    if(secondsPassed > 2) {
      collisionOccured = true;
      document.querySelector("#score-text").textContent
      = 'Game over, your final score:  ' + secondsPassed + ' (refresh the web page to restart)';
      if(saved_high_score == false) {
         $.ajax({
            type: "POST",
            dataType: "json",
            url: "/post_highscore",
            data: {
              "score": secondsPassed
            },
            success: function(data) {
                console.log(data);
            },
        });
        saved_high_score = true;
      }
    }
  }
  requestAnimationFrame( animate );

  renderer.render(scene, camera);
			};
  animate();
}

}