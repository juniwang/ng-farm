app.directive('seedInfo', function() { 
  return { 
    restrict: 'E', 
    scope: {
        info: "="
    }, 
    templateUrl: '/static/js/directives/seedInfo.html' 
  }; 
});