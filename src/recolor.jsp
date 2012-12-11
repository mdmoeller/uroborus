<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>

<title>Recolor</title>
</head>
<%@page import="java.util.*" %>
<%@page import="uroborus.*" %>


<%

String threshold = request.getParameter("threshold");
uroborus.CreateHtml.takeInput(threshold);

String pkg = request.getParameter("packagename");
response.sendRedirect(pkg + "_report.html");

%>


<body>

</body>
</html>
