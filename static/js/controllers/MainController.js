app.directive('fileModel', ['$parse', function ($parse) {
  return {
     restrict: 'A',
     link: function(scope, element, attrs) {
        var model = $parse(attrs.fileModel);
        var modelSetter = model.assign;
        
        element.bind('change', function() {
           scope.$apply(function() {
              modelSetter(scope, element[0].files[0]);
           });
        });
     }
  };
}]);

app.service('fileUpload', ['$https:', function ($https) {
  this.uploadFileToUrl = function(file, uploadUrl) {
     var fd = new FormData();
     fd.append('file', file);
  
     $https.post(uploadUrl, fd, {
        transformRequest: angular.identity,
        headers: {'Content-Type': undefined}
     })
     .success(function() {
     })
     .error(function() {
     });
  }
}]);

app.controller('MainController', ['$scope', '$http', '$log', function ($scope, $http, $log) {
  //chart definition
  $scope.keywordToggle = true;
  $scope.uploadToggle = true;
  $scope.formToggle = false;
  $scope.formData = {};
  $scope.textAreaToggle = false;
  $scope.showLoader = false;
  $scope.fileToggle = false;

  $scope.uploadFunc = function () {
    let bool = $scope.keywordToggle;
    bool = bool ? false : true;
    $scope.keywordToggle = bool;
    $scope.formToggle = false;
    $scope.fileToggle = $scope.fileToggle ? false : true;
  };

  $scope.keywordFunc = function () {
    $scope.uploadToggle = $scope.uploadToggle ? false : true;
    $scope.formToggle = $scope.formToggle ? false : true;
    $scope.formData.summaryInput = "";
    $scope.textAreaToggle = false;
    $scope.fileToggle = false;
  };

  $scope.getSummaryFromFile = function () {
    var file = $scope.myFile;
               console.log('file is ' );
               console.dir(file);
               var uploadUrl = "/fileUpload";
               fileUpload.uploadFileToUrl(file, uploadUrl);
    $http({
      url: '/text/ocr',
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      data : {file : "/fileUpload/" + $scope.myFile}
    
    }).success(function (results) {
      $scope.showLoader = false;
      $scope.textAreaToggle = true;
      $scope.textAreaToggle = true;
      $scope.summary = results.data
    }).error(function (error) {
      //$log.log(error);
    });
  }

  $scope.getSummary = function () {
    console.log($scope.formData.summaryInput);
    $scope.showLoader = true;
    $scope.textAreaToggle = false;
    $http({
      url: '/summarize',
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      data: JSON.stringify({ text: $scope.formData.summaryInput, isHeading: 1 })
    }).success(function (results) {
      $scope.showLoader = false;
      $scope.textAreaToggle = true;
      $scope.textAreaToggle = true;
      $scope.summary = results.data
    }).error(function (error) {
      //$log.log(error);
    });
  }

  $scope.getQuiz = function () {
    $http({
      url: '/question',
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      data: JSON.stringify({ text: $scope.summary, isFormatted: 1 })
    }).success(function (results) {
      $scope.questions = results.data;
      
    }).error(function (error) {
      //$log.log(error);
    });
  }

}]).config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});;;


