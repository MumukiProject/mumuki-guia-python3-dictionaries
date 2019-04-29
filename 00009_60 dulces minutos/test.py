describe("", function() {
  it("Un postre de una hora y media no es rápido", function() {
    postreDeLeche = {ingredientes:["leche"], tiempoDeCoccion:90}
    assert.equal(postresRapidos.length, 2);
  })
  
  it("Un postre de media hora es rápido", function() {
    postreDeLeche = {ingredientes:["leche"], tiempoDeCoccion:30}
    agregarAPostresRapidos(postreDeLeche);
    assert.equal(postresRapidos.length, 3);
    assert.equal(postresRapidos.slice(-1).pop(), postreDeLeche);
  })
})