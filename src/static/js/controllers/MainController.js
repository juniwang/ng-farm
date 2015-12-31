app.controller('MainController', ['$scope', function($scope) {
    $scope.title='Top 5 Sellers';
    $scope.seeds = [
        {
            "name": "Nexus S",
            "number": 123
        },
        {
            "name": "Motorola XOOM™ with Wi-Fi",
            "number": 2345
        },
        {    
            "name": "MOTOROLA XOOM™",
            "number": 4444
        }
    ];
}]);