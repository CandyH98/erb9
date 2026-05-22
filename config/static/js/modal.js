$(document).ready(()=>{
    $('#deleteConfirmModal').on("show.bs.modal", (e)=>{
        const button = $(e.relatedTarget); 
        const contactId = button.data('id'); 
        const deleteUrl = button.data('url'); 
        $('#modal-contact-id').text(contactId);
        $('#confirmDeleteBtn').attr('href', deleteUrl);
    })

    $('#confirmDeleteBtn').click((e)=>{
        $('#deleteConfirmModal').modal('hide');
        setTimeout(()=>{
            window.location.href = $('#confirmDeleteBtn').attr('href');
        },300);
    })
});
