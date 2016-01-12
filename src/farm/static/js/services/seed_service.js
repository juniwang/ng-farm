app.factory('ses', ['$http', function($http){
    return  {
        getSeedList: function(){
            return $http.get('/api/farm/seed/list')
        },
        disable: function(name){
            return $http.delete("/api/farm/seed/"+name)
        },
        del: function(name){
            return $http.delete("/api/farm/seed/"+name + "?del=1")
        },
        getRecylceList: function(){
            return $http.get('/api/farm/seed/list?del=1&limit=10') 
        },
        update: function(name, data){
            return $http.post("/api/farm/seed/"+name, data)
        },
        getAllSeeds: function(){
            return $http.get('/api/farm/seeds') 
        }
    }
}]);