app.controller('MainController', ['$scope', 'ses', '$location', "$timeout", function($scope, ses, $location, $timeout) {

    $scope.alerts = [];

    $scope.isActive = function (viewLocation) {
        if( $location.path() == "" )
            return viewLocation==="/plant"

        var active = (viewLocation === $location.path());
        return active;
    };

    $scope.addAlert = function (alertObj, duration) {
        var newAlertObj = alertObj;
        newAlertObj.uid = Math.floor(Math.random() * 100000);
        var alertIndex;

        $scope.alerts.push(newAlertObj);

        if (duration !== 'stay') {
            $timeout(function () {
                for (var i = 0; i < $scope.alerts.length; i++) {
                    if ($scope.alerts[i].uid === newAlertObj.uid) {
                        alertIndex = i;
                        break;
                    }
                }
                $scope.alerts.splice(alertIndex, 1);
            }, duration || 2500);
        }
    };

    $scope.closeAlert = function (index) {
        $scope.alerts.splice(index, 1);
    };


    var load_plants = function(){
        return ses.getSeedList().success(function(data){
            $scope.plants = data
        });
    }

    var load_sells = function(){
        return ses.getRecylceList().success(function(data){
            $scope.sells = data
        });
    }

    var load_all = function(){
        return ses.getAllSeeds().success(function(data){
            $scope.all_seeds = data
        })
    }

    $scope.cur = 1

    var set_seeds = function(){
        if($scope.cur==1){
            $scope.seeds = $scope.plants
        }else if($scope.cur==2){
            $scope.seeds = $scope.sells
        }else{
            $scope.seeds = $scope.all_seeds
        }
    }

    var reload = function(){
        load_plants()
        load_sells()
        load_all().success(function(){
            set_seeds()
        })
    }


    var reset_form = function(){
        $scope.seedName = ""
        $scope.seedNumber = "-1"
    }

    $scope.view_all = function(){
        $scope.cur = 3
        set_seeds()
    }

    $scope.view_plants = function(){
        $scope.cur = 1
        set_seeds()
    }

    $scope.view_sells = function(){
        $scope.cur = 2
        set_seeds()
    }

    $scope.delete_seed = function(name){
        return ses.del(name).success(function(data){
            $scope.addAlert({type: 'success', msg: 'The seed ' + name+' is deleted from cloud successfully.'});
            reload();
        }).error(function(err){
            $scope.addAlert({type: 'danger', msg: 'Operation fails due to some internal server error!'});
        })
    };

    $scope.complete_seed = function(name){
        ses.disable(name).success(function(data){
            $scope.addAlert({type: 'success', msg: 'The seed ' + name+' is completed in cloud.'});
            reload();
        }).error(function(err){
            $scope.addAlert({type: 'danger', msg: 'Operation fails due to some internal server error!'});
        })
    };

    $scope.update_seed_in_form = function(){
        name = $scope.seedName
        num = $scope.seedNumber
        ses.update(name, {number: num}).success(function(data){
            $scope.addAlert({type: 'success', msg: 'The seed ' + name+' is saved to cloud successfully.'});
            reload();
            reset_form();
        }).error(function(err){
            $scope.addAlert({type: 'danger', msg: 'Operation fails due to some internal server error!'});
        })
    };

    $scope.del_in_form = function(){
        name = $scope.seedName
        $scope.delete_seed(name).success(function(){
            reset_form();
        })
    };

    reload()
}]);