

const My = new class{
	constructor(){
		$(document).on("keyup", "#loginForm input:text, #loginForm input:password", (evt) => {
			const th = $(evt.target)
			const sibling = th.is("input:text")?th.siblings("input:password"):th.siblings("input:text")
			let clsName = (th.val().length >= 3 && sibling.val().length >= 3)?'removeClass':'addClass'
			$(".sendButton")[clsName]("disabled")
		})

	}

	formSubmit(ths, needReload){
		const th = $(ths)
		const button = $(".sendButton", th)
		if(button.is(".disabled"))return false
		if(needReload != null){
			setTimeout(() => {
				location.reload()
			}, 500)
		}
		return true
	}

	uploadImages(evt){
		let iter = 0
		console.log("some")
		if(evt.target.files && evt.target.files.length){
			if(evt.target.files[0]){
				let modal = $("#exampleModal")
				let list = $(".list-group", modal)
				let obj = {}
				obj.name = evt.target.files[0].name.replace(/\s/g, '_').toLowerCase() 
				obj.ext = obj.name.split('.').pop().substring(0, 20)
				obj.name = obj.name.substring(0, 20)+'..'
				obj.size = (evt.target.files[0].size / 1024).toFixed(2)+" kg"
				if(!['xlsx','xls'].includes(obj.ext)){
					$('.sendButton', modal).addClass("disabled")
					list.addClass("display_none")
					alert('allowed file formats: .xls, .xlsx')
					return
				}
				
				list.removeClass("display_none")
				Object.keys(obj).forEach((v) => {
					$("span."+v+"", list).text(obj[v])
				})
				$('.sendButton', modal).removeClass("disabled")
			}
			
		}
	}


}