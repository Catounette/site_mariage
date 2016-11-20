function init_map(){
	var latlng = new.google.maps.Latlng();
	var options={zoom:10,
		center=latlng,
		mapTypeId:google.maps.mapType.ROADMAP
	};
	map=new google.maps.Map(latlng,options);
}