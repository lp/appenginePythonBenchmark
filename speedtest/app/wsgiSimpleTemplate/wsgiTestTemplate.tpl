<html>
<body>
    <table>
    %for i in range(numA):
        <tr><td>{{i}}</td><td>x {{numB}}</td><td>= {{i * numB}}</td></tr>
    %end
    </table>
</body>
</html>