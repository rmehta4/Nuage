var rutvijTodo = angular.module('rutvijTodo', []);

rutvijTodo.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
 }); // made it flask compatible


function mainController($scope, $http) {
        $scope.formData = {};
        // when landing on the page, get all todos and show them
        $http.get('/api/todos')
                .success(function(data) {
                        $scope.todos = data.result;
                        console.log(data.result);
                })
                .error(function(data) {
                        console.log('Error: ' + data);
                });

        $scope.getToDo = function(){
        $http.get('/api/todos')
                .success(function(data) {
                        $scope.todos = data.result;
                        console.log(data.result);
                })
                .error(function(data) {
                        console.log('Error: ' + data);
                });
        };
        // when submitting the add form, send the text to the flask API
        $scope.createTodo = function() {
                $http.post('/api/todos', $scope.formData)
                        .success(function(data) {
                                $scope.formData = {}; // clear the form
                                $scope.todos = data;
                                $scope.getToDo('api/todos');
                        })
			.error(function(data) {
                                console.log('Error: ' + data);
                        });
        };

        // delete a todo after checking it
        $scope.deleteTodo = function(id) {
                $http.delete('/api/todos/'+id)
                        .success(function(data) {
                                $scope.todos = data;
                                $scope.getToDo('api/todos');
                        })
                        .error(function(data) {
                                console.log('Error: ' + data);
                        });
        };

}


