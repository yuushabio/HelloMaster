angular.module('starter.controllers', ['ngCordova'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout, $state) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});
  
  //function to direct you to category page
   $scope.category = function(category){
	$state.go('app.category', {category_name_id:category});
	//$scope.category_name_id = $state.params.category_name_id;
  }
  
  
  /*SIGN UP MODAL*/
  // Create the signup modal that we will use later
  $ionicModal.fromTemplateUrl('templates/signup.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modalSignUp = modal;
  });

  // Triggered in the signup modal to close it
  $scope.closeSignUp = function() {
    $scope.modalSignUp.hide();
	$state.go('app.home', {}, {reload: true});
  };

  // Open the signup modal
  $scope.signup = function() {
    $scope.modalSignUp.show();
	$scope.modalLogIn.hide();
  };

  // Perform the signup action when the user submits the signup form
  // Form data for the signup modal
  $scope.SignUpData = {};
  $scope.doSignUp = function() {
    console.log('Doing signUp', $scope.SignUpData);

    // Simulate a signup delay. Remove this and replace with your signup
    // code if using a signup system
    $timeout(function() {
      $scope.closeSignUp();
    }, 1000);
  };
  /*END OF MODAL*/
  
  
  
  
  /*LOG IN MODAL*/
  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modalLogIn = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogIn = function() {
    $scope.modalLogIn.hide();
	$state.go('app.home', {}, {reload: true});
  };

  // Open the login modal
  $scope.LogIn = function() {
    $scope.modalLogIn.show();
	$scope.modalSignUp.hide();
  };

  // Perform the login action when the user submits the login form
  // Form data for the login modal
  $scope.LogInData = {};
  $scope.doLogIn = function() {
    console.log('Doing login', $scope.LogInData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogIn();
    }, 1000);
  };
  /*END OF MODAL*/
  
  
  
})


.controller('categoryCtrl', function($scope, $stateParams,$state) {
	$scope.category_name_id = $state.params.category_name_id; //scope for getting artist name dynamically
	
	$scope.products = [
		{ product_name: 'Reggae', id: 1 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png' , price: 'GH¢ 1', category: 'Electronics',location:'Unity'},
		{ product_name: 'Chill', id: 2, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 5', category: 'Clothings',location:'Katanga'},
		{ product_name: 'Dubstep', id: 3, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 10', category: 'Electronics',location:'Engineering gate'},
		{ product_name: 'Indie', id: 4, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 3', category: 'Electronics',location:'Africa'},
		{ product_name: 'Rap', id: 5 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Electronics',location:'Republic'},
		{ product_name: 'Cowbell', id: 6 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Electronics',location:'Hall 7'},
		{ product_name: 'New Product', id: 7 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Gadgets',location:'Brunei'}
	];
})


.controller('myAdsController', function($scope, $stateParams,$state) {
	$scope.addAds = function(){
		$state.go('app.addAds');
	}
	$scope.products = [
		{ product_name: 'Reggae', id: 1 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png' , price: 'GH¢ 1', category: 'Electronics',location:'Unity'},
		{ product_name: 'Chill', id: 2, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 5', category: 'Clothings',location:'Katanga'},
		{ product_name: 'Dubstep', id: 3, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 10', category: 'Electronics',location:'Engineering gate'},
		{ product_name: 'Indie', id: 4, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 3', category: 'Electronics',location:'Africa'},
		{ product_name: 'Rap', id: 5 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Electronics',location:'Republic'},
		{ product_name: 'Cowbell', id: 6 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Electronics',location:'Hall 7'},
		{ product_name: 'New Product', id: 7 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Gadgets',location:'Brunei'}
	];
})

/*controller for home*/
.controller('homeCtrl', function($scope, $stateParams, $state) {
	$scope.item_id = $state.params.item_id; 
	$scope.products = [
		{ product_name: 'Reggae', id: 1 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png' , price: 'GH¢ 1', category: 'Electronics',location:'Unity'},
		{ product_name: 'Chill', id: 2, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 5', category: 'Clothings',location:'Katanga'},
		{ product_name: 'Dubstep', id: 3, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 10', category: 'Electronics',location:'Engineering gate'},
		{ product_name: 'Indie', id: 4, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 3', category: 'Electronics',location:'Africa'},
		{ product_name: 'Rap', id: 5 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante. ' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Electronics',location:'Republic'},
		{ product_name: 'Cowbell', id: 6 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Electronics',location:'Hall 7'},
		{ product_name: 'New Product', id: 7 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante. ' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Gadgets',location:'Brunei'}
	];
})

.controller('addAdsCtrl',function($scope, $ionicPlatform){
	
	$scope.images = [];
	
	 var options = {
	   maximumImagesCount: 1,
	   width: 800,
	   height: 800,
	   quality: 80
	  };
	
	
	$scope.getImage = function(){
		
		window.imagePicker.getPictures(options)(
			function(results) {
				for (var i = 0; i < results.length; i++) {
					console.log('Image URI: ' + results[i]);
					$scope.images.push(results[i]);
					alert(results[i]);
				}
				//if(!$scope.$$phase) {
				//	$scope.$apply();
				//}
			}, function (error) {
				console.log('Error: ' + error);
			}
		);
		
		
	}
	
	
	
	
})

/*controller for the item page*/
.controller('itemCtrl', function($scope, $stateParams,$state) {
	$scope.goback = function(){
		$state.go('app.home');
	}
	
	$scope.product_item_id = $state.params.product_item_id; //scope for getting artist name dynamically
	$scope.products = [
		{ product_name: 'Reggae', id: 1 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png' , price: 'GH¢ 1', category: 'Electronics',location:'Unity'},
		{ product_name: 'Chill', id: 2, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 5', category: 'Clothings',location:'Katanga'},
		{ product_name: 'Dubstep', id: 3, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 10', category: 'Electronics',location:'Engineering gate'},
		{ product_name: 'Indie', id: 4, description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 3', category: 'Electronics',location:'Africa'},
		{ product_name: 'Rap', id: 5 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante. ' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Electronics',location:'Republic'},
		{ product_name: 'Cowbell', id: 6 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante.' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Electronics',location:'Hall 7'},
		{ product_name: 'New Product', id: 7 , description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque viverra mauris id enim laoreet, non aliquam felis mattis. Praesent metus tortor, viverra in ultricies ut, iaculis sit amet neque. Suspendisse eget commodo ante. ' , image: 'img/side_menu.png', price: 'GH¢ 1', category: 'Gadgets',location:'Brunei'}
	];
});

