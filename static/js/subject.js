function Populate(f1 , f2)
{
           var optionArray;
           var f1 = document.getElementById(f1);
           var f2 = document.getElementById(f2);
           f2.innerHTML = "";
           if (f1.value === "Middel")
           {
               optionArray = ["Science | Science", "Arts | Arts"];
           }
           else if (f1.value === "Nineth")
           {
               optionArray = [ "Bio | Bio", "Computer | Computer", "Arts | Arts"];
           }
           else if (f1.value === "Tenth")
           {
               optionArray = ["Bio | Bio", "Computer | Computer", "Arts | Arts"];
           }
           else if (f1.value === "First year")
           {
               optionArray = ["Bio | Pre medical", "Maths | Pre engeniering", "Computerstat | Ics-Stat","Computerphy | Ics-Phy","Computereco | Ics-Eco","Icom | Icom","Fa | F.A"];
           }
           else if (f1.value === "Second year")
           {
               optionArray = ["Bio | Pre medical", "Maths | Pre engeniering", "Computerstat | Ics-Stat","Computerphy | Ics-Phy","Computereco | Ics-Eco","Icom | Icom","Fa | F.A"];
           }
           else
           {
               optionArray = ["|"];
           }
           for (var choice in optionArray)
           {
                var pair = optionArray[choice].split("|");
                var newoption = document.createElement("option");
                newoption.value = pair[0];
                newoption.innerHTML =pair[1];
                f2.options.add(newoption);
           }
}
function Cla()
{
    document.getElementById("clas-field").multiple = true;
}
function Subjects()
{
    document.getElementById("sub-field").multiple = true;
}