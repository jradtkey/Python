function main() {
   const listA = [
    {id: 0, name: 'A'},
    {id: 2, name: 'C'},
    {id: 11, name: 'R'},
    {id: 4, name: 'E'},
    {id: 7, name: 'T'},
    {id: 13, name: 'Y'},
    {id: 5, name: 'C'},
    {id: 3, name: 'I'},
    {id: 6, name: 'C'},
    {id: 9, name: 'O'},
    {id: 1, name: 'V'},
   ]

/*
1. Write a function to transform list of objects (listA) to list of objects (listB) in
   such a way that "name" would be formatted as "name-id".
   So for example "{id: 0, name: 'A'}" should become "{id: 0, name: 'A-0'}"
*/

    function transform(listA) {
      var newList = []
      for (var i = 0; i < listA.length; i++) {
        var obj = {};
        obj.id = listA[i].id;
        obj.name = listA[i].name + '-' + listA[i].id
        newList.push(obj)
      }
      return newList;
    }

    const listB = transform(listA)
    console.log(listB)


/*
2. Write a function to transform list of objects (listA) to list of objects (listC)
   in such a way that only object with id=2 will be changed, set it's name to "Fox". All other
   objects should not be modified.
*/

    function transformFox(listA) {
      var newList = []
      for (var i = 0; i < listA.length; i++) {
        var obj = {};
        if (listA[i].id == 2) {
          obj.id = listA[i].id;
          obj.name = 'Fox';
          newList.push(obj)
        }
        else {
          newList.push(listA[i])
        }
      }
      return newList
    }
    const listC = transformFox(listA)
    console.log(listC)


/*
3. Write a function that does the following:
  * filters a list of objects (listA) in such a way, so new list contains only
  items with odd ids
  * sorts items by id in ascending order
  * combines all names from all items into one string

  E.g. if after filtering and sorting you got:
   [   {id: 1, name: 'A'},
       {id: 3, name: 'B'}, ]
   then result should be:
   'AB'
*/

    function transformOdd(listA) {
      var newList = []
      var newString ='';

      for (var i = 0; i < listA.length; i++) {
        if (listA[i].id % 2 !== 0) {
          newList.push(listA[i]);
        }
      }

      newList.sort(function(a,b){
        return a.id-b.id
      });

      for (var i = 0; i < newList.length; i++) {
        newString += newList[i].name
      }
      return newString
    }

    const oddObject = transformOdd(listA)
    console.log(oddObject)


/*
  Task 4, using two lists, "customers" and "invoices", merge them together by "id + customerId"
	so result is same as "invoices", but with new property "customerName" from corresponding customer attached to it
*/

    const invoices = [{
  	id: 1,
  	total: 10,
  	customerId: 1
    }, {
  	id: 2,
  	total: 20,
  	customerId: 2
    }, {
  	id: 3,
  	total: 30,
  	customerId: 4
    }]

  	const customers = [{
  		id: 1,
  		name: 'Brian'
  	}, {
  		id: 2,
  		name: 'Mary'
  	}, {
  		id: 3,
  		name: 'John'
  	}]

  	function addCustomerNamesToInvoices(invoices, customers) {
      for (var i = 0; i < invoices.length; i++) {
        for (var j = 0; j < customers.length; j++) {
          if (customers[j].id == invoices[i].customerId) {
            invoices[i].customerName = customers[j].name
          }
        }
      }
      return invoices
  	}

  	const invoicesWithNames = addCustomerNamesToInvoices(invoices, customers)
  	console.log(invoicesWithNames)

}

main()
