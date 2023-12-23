<template lang="">
    <nav  class="navbar navbar-expand-lg border-bottom border-white border-danger">
        <div class="container mh-100 ">
            <a style="color: red; font-size: xxx-large; font-family: SmoochSansSemiBold;" class="navbar-brand logo" href="">
                STATMANN
                <!-- <img class="" src="../assets/images/Group 11.png" alt=""> -->
            </a>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                <a class="nav-link active text-white mx-4" aria-current="page" href="#">
                    debates</a>
                <a class="nav-link active text-white mx-4" aria-current="page" href="#">results / fixtures</a>
                <a class="nav-link active text-white mx-4" aria-current="page" href="blog">alerts</a>
                <a class="nav-link active text-white mx-4" aria-current="page" href="blog">live scores</a>
                </div>
            </div>
            <div>
                <a style="font-family: SmoochSansSemiBold" class="text-decoration-none text-danger" href="">mikeyfennelly1</a>
                <img class="ms-4" src="../assets/images/profilePhoto.png" alt="">
            </div>
        </div>
    </nav>

</template>
<script>

export default {
    name: 'NavbarItem',
    props: {
        type: String
    }
}
</script>
<style lang="css">
    nav {
        font-family: SmoochSans;
        font-size: x-large;
    }
    .logo {
        font-size: xx-large;
    }
    img {
        max-height: 25px;
    }
</style>